"""
统一画图样式，供外部脚本 import 使用
"""
import matplotlib as mpl
mpl.rcParams['figure.dpi']      = 150
mpl.rcParams['font.size']       = 10
mpl.rcParams['lines.linewidth'] = 1.2
mpl.rcParams['axes.grid']       = True
mpl.rcParams['grid.alpha']      = 0.3