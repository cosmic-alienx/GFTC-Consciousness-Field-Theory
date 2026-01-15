"""
实验二：二维参数扫描 (μ, λ_c) → 相图热力图
"""
import numpy as np
import matplotlib.pyplot as plt
from gftc_core import GFTC_ToyModel

mu_vals    = np.linspace(0.005, 0.04, 16)
lambda_vals= np.linspace(0.01, 0.06, 20)
ORDER = np.zeros((len(mu_vals), len(lambda_vals)))

for i, mu in enumerate(mu_vals):
    for j, lam in enumerate(lambda_vals):
        print(f"[+] μ={mu:.3f}  λ_c={lam:.3f}")
        model = GFTC_ToyModel(mu=mu, lambda_c=lam, nsteps=3000)
        order_hist = model.evolve()
        ORDER[i, j] = np.mean(order_hist[-10:])

# 绘图
plt.figure(figsize=(5,4))
plt.imshow(ORDER, aspect='auto', origin='lower',
           extent=[lambda_vals[0], lambda_vals[-1], mu_vals[0], mu_vals[-1]],
           cmap='inferno', vmin=0)
plt.colorbar(label='order parameter')
plt.xlabel(r'consciousness coupling $\lambda_c$')
plt.ylabel(r'neural instability $\mu$')
plt.title('2D phase diagram of consciousness')
plt.tight_layout()
plt.savefig('figures/figure2_2d_phase_diagram.png', dpi=300)
plt.show()