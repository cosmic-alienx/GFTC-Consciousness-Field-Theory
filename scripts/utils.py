"""
通用小工具，例如离散 Laplacian（若不想用谱方法）
"""
import numpy as np

def laplacian_2d(f, dx=1.0):
    """四阶中心差分 Laplacian，周期边界"""
    return (np.roll(f, -1, axis=0) + np.roll(f, 1, axis=0) +
            np.roll(f, -1, axis=1) + np.roll(f, 1, axis=1) - 4*f) / dx**2