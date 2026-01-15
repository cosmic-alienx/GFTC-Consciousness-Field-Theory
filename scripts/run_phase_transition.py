"""
实验一：单参数扫描 λ_c → 秩序度跃迁曲线
"""
import numpy as np
import matplotlib.pyplot as plt
from gftc_core import GFTC_ToyModel

lambda_range = np.linspace(0.01, 0.06, 21)
order_mean = []

for lam in lambda_range:
    print(f"[+] running λ_c = {lam:.3f}")
    model = GFTC_ToyModel(lambda_c=lam, nsteps=3000)
    order_hist = model.evolve()
    # 取后 1/3 平均作为稳态值
    order_mean.append(np.mean(order_hist[-10:]))

# 绘图
plt.figure(figsize=(5,3.5))
plt.plot(lambda_range, order_mean, 'o-')
plt.axvline(0.032, ls='--', c='grey', label='critical λ_c ≈ 0.032')
plt.xlabel(r'consciousness coupling $\lambda_c$')
plt.ylabel('order parameter 〈|∇×A|〉')
plt.title('Phase transition of consciousness')
plt.legend()
plt.tight_layout()
plt.savefig('figures/figure1_phase_transition.png', dpi=300)
plt.show()