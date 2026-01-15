# 意识几何场论（GFTC）——数值模型  

本仓库提供了「意识几何场论」（Geometric Field Theory of Consciousness, GFTC）的**数值实现**。  
该理论将意识视为一种**宏观几何有序态**，通过在二维格点上的多耦合场发生**动力学相变**而涌现。

---

## 🌟 核心发现

1. **临界阈值**  
   存在明确的*意识耦合*临界值  
   `λ_c^crit ≈ 0.032`。  
   低于该值系统处于无序态；一旦越过，规范场立即自发形成**稳定涡旋晶格**。

2. **协同相图**  
   意识**并非**由单一参数控制。  
   在 `(μ, λ_c)` 平面上扫描得到一条**倾斜的相边界**，将「无意识」与「有意识」区域分开，表明  
   **「神经准备度」**与**「全局整合效率」**必须协同配合才能涌现意识。

---

## 🗂️ 仓库结构

```新建文件夹
GFTC-Consciousness-Field-Theory/
├── scripts/
│   ├── gftc_core.py              # 格点模型与梯度下降演化
│   ├── run_phase_transition.py   # 实验一：单参数 λ_c 扫描
│   ├── run_2d_phase_diagram.py   # 实验二：(μ, λ_c) 相图
│   ├── utils.py                  # 离散拉普拉斯等工具
│   └── plot_results.py           # 统一绘图风格
├── figures/                      # 自动生成图片（需先创建文件夹）
├── requirements.txt              # NumPy + Matplotlib
└── README.md                     # 本文件
```

---

## 🚀 快速上手

1. **克隆与安装**  
   ```bash
   git clone https://github.com/YOUR_USERNAME/GFTC-Consciousness-Field-Theory.git
   cd GFTC-Consciousness-Field-Theory
   pip install -r requirements.txt
   ```

2. **运行核心实验**  
   - *实验一*——临界现象：  
     ```bash
     python scripts/run_phase_transition.py
     ```  
     ➜ 生成 `figures/figure1_phase_transition.png`

   - *实验二*——二维相图：  
     ```bash
     python scripts/run_2d_phase_diagram.py
     ```  
     ➜ 生成 `figures/figure2_2d_phase_diagram.png`

3. **探索与修改**  
   所有物理逻辑封装在 `scripts/gftc_core.py` 的 `GFTC_ToyModel` 类中，  
   可随意调整格点大小、势函数、耦合形式、初始条件等。

---

## 📈 可复现结果

| 图 | 描述 | 科学意义 |
|----|------|----------|
| `figure1_phase_transition.png` | 序参量随 `λ_c` 突跳及其导数峰值；插图显示 `∇ × A` 从噪声演变为清晰涡旋。 | 首次为「意识耦合存在临界阈值」提供**计算证据**。 |
| `figure2_2d_phase_diagram.png` | `(μ, λ_c)` 平面序参量热力图，呈现倾斜相边界与高序「高原」。 | 表明意识是「神经易激性」与「全局整合」**协同产物**，为麻醉、睡眠、清醒等状态提供**统一理论坐标**。 |

---

## 🔧 模型速览

**二维周期格点上的三条场**  
- `Ψ`（复标量）——*神经活动场*  
- `φ`（实标量）——*因果密度场*（双稳势）  
- `A_μ = (Ax, Ay)`——*U(1) 规范场*，其旋度即为**意识的几何印记**

**离散作用量**  
```
S = Σ[ |Dψ|² + V_ψ(ψ) + ½(∇φ)² + V_φ(φ) + ¼ F_{μν}F^{μν}
     + λ_c φ |ψ|²  +  μ φ² ] Δ²x
```
其中 `D_μ = ∇_μ - i A_μ`，`F_{μν}` 为规范场强。

**动力学**  
虚构时间梯度下降 → 系统流向**低能态**。  
序参量 = **`∇ × A` 的空间标准差**。

---

## 🧠 理论背景与延伸阅读

GFTC 试图弥合「解释鸿沟」，核心映射：

- **感受质**→ 高维经验空间截面的几何，  
- **意识统一性**→ 纤维丛全局截面的存在，  
- **心–物互动**→ 规范不变耦合项。

完整的数学推导、哲学动机及与整合信息论（IIT）等理论的比较，详见即将发布的预印本（链接稍后更新）。

---

## 🤝 欢迎贡献

- 对模型假设、数学或哲学有疑问？  
- 想优化代码、报 Bug、加功能？  
- 有新实验点子（注意力切换、病理状态…）？

请直接开 **[GitHub Issue](https://github.com/YOUR_USERNAME/GFTC-Consciousness-Field-Theory/issues)**，一起探索**意识的几何疆域**！

---

## 📜 引用与许可

若本代码或思路对你的研究有启发，请：

- 引用本仓库链接；  
- 在论文中注明：  
  *「GFTC（意识几何场论）数值玩具模型」*

项目采用 **MIT 许可证**，可自由使用、修改与分发，但请保留原始版权说明。

---

**探索者寄语**：  
意识或许是宇宙最复杂的现象，却绝非不可触碰的神秘。这个玩具模型是一把粗糙但坚定的钥匙，期待与你一起将它打磨得更锋利。
```
