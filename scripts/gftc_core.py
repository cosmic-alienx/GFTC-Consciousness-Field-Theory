"""
意识几何场论（GFTC）玩具模型
二维周期格点 + 三条场（Ψ, φ, A）+ 梯度下降弛豫
"""
import numpy as np
from numpy.fft import fft2, ifft2

class GFTC_ToyModel:
    """
    参数全部用 SI 单位归一化，可任意调节。
    """
    def __init__(self, L=128, dx=1.0,
                 mu=0.02,           # 神经底物不稳定性
                 lambda_c=0.03,     # 全局意识耦合
                 nsteps=2000,       # 梯度下降步数
                 dt=0.01,           # 步长
                 seed=42):
        self.L, self.dx = L, dx
        self.mu = mu
        self.lambda_c = lambda_c
        self.nsteps = nsteps
        self.dt = dt
        np.random.seed(seed)

        # 场初始化
        self.psi = 0.1 * (np.random.randn(L, L) + 1j * np.random.randn(L, L))
        self.phi = np.tanh(np.random.randn(L, L))   # 双稳态初始
        self.Ax  = 0.01 * np.random.randn(L, L)
        self.Ay  = 0.01 * np.random.randn(L, L)

        # 动量空间 Laplacian
        k = 2 * np.pi * np.fft.fftfreq(L, d=dx)
        self.kx, self.ky = np.meshgrid(k, k, indexing='ij')
        self.k2 = self.kx**2 + self.ky**2

    # ---------------- 能量泛函的局部项 ----------------
    def V_psi(self, psi):
        """Ψ 自作用势 |ψ|^4 - |ψ|^2 """
        return -np.abs(psi)**2 + 0.5 * np.abs(psi)**4

    def V_phi(self, phi):
        """φ 双稳态势  (φ^2-1)^2 """
        return (phi**2 - 1)**2

    # ---------------- 梯度下降更新 ----------------
    def update_fields(self):
        """一步梯度下降，全部用谱方法算 Laplacian"""
        # 方便写法
        psi, phi, Ax, Ay = self.psi, self.phi, self.Ax, self.Ay

        # --- 1. 更新 ψ ---
        lap_psi = ifft2(-self.k2 * fft2(psi))
        dVdpsi = -psi + np.abs(psi)**2 * psi
        # 与 φ 耦合项
        coup_psi = self.lambda_c * phi * psi
        psi_new = psi - self.dt * (lap_psi / self.dx**2 + dVdpsi + coup_psi)

        # --- 2. 更新 φ ---
        lap_phi = ifft2(-self.k2 * fft2(phi))
        dVdphi = 4 * phi * (phi**2 - 1)
        # 与 |ψ|^2 耦合
        coup_phi = 0.5 * self.lambda_c * np.abs(psi)**2
        phi_new = phi - self.dt * (lap_phi / self.dx**2 + dVdphi + coup_phi)

        # --- 3. 更新 A（简化：仅 dissipate）---
        lap_Ax = ifft2(-self.k2 * fft2(Ax))
        lap_Ay = ifft2(-self.k2 * fft2(Ay))
        Ax_new = Ax - self.dt * lap_Ax / self.dx**2
        Ay_new = Ay - self.dt * lap_Ay / self.dx**2

        # 同步
        self.psi, self.phi = psi_new, phi_new
        self.Ax,  self.Ay  = Ax_new, Ay_new

    # ---------------- 序参量 ----------------
    def order_parameter(self):
        """规范场旋度的空间平均作为秩序度"""
        curlA = (np.roll(self.Ay, -1, axis=0) - np.roll(self.Ay, 1, axis=0)) / (2*self.dx) \
              - (np.roll(self.Ax, -1, axis=1) - np.roll(self.Ax, 1, axis=1)) / (2*self.dx)
        return float(np.std(curlA))

    # ---------------- 主演化 ----------------
    def evolve(self):
        """跑完 nsteps，每 100 步返回一次 order"""
        hist = []
        for step in range(self.nsteps):
            self.update_fields()
            if step % 100 == 0:
                hist.append(self.order_parameter())
        return hist