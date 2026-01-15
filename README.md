# Geometric Field Theory of Consciousness (GFTC) – Numerical Toy Model  
*(English version of the README)*

This repository provides a **numerical implementation** of the *Geometric Field Theory of Consciousness* (GFTC).  
The theory regards consciousness as a **macroscopic geometric order** that emerges through a **dynamical phase transition** in a multi-field system defined on a 2-D lattice.

---

## 🌟 Key Findings

1. **Critical Threshold**  
   There is a sharp critical value of the *consciousness coupling*  
   `λ_c^crit ≈ 0.032`.  
   Below `λ_c^crit` the system stays disordered; above it a highly ordered
   vortex-lattice of the gauge field appears **abruptly**.

2. **Synergistic Phase Diagram**  
   Consciousness is **not** controlled by a single parameter.  
   A 2-D sweep of *neural instability* `μ` vs. `λ_c` reveals a **tilted phase
   boundary** separating unconscious from conscious regions, implying that
   **“neural readiness”** and **“global integration”** must cooperate.

---

## 🚀 Quick Start

1. **Clone & install**  
   ```bash
   git clone https://github.com/YOUR_USERNAME/GFTC-Consciousness-Field-Theory.git
   cd GFTC-Consciousness-Field-Theory
   pip install -r requirements.txt
   ```

2. **Run the core experiments**  
   - *Experiment 1* – critical phenomenon:  
     ```bash
     python scripts/run_phase_transition.py
     ```  
     ➜ produces `figures/figure1_phase_transition.png`

   - *Experiment 2* – 2-D phase diagram:  
     ```bash
     python scripts/run_2d_phase_diagram.py
     ```  
     ➜ produces `figures/figure2_2d_phase_diagram.png`

3. **Explore & modify**  
   All physics is encapsulated in the class `GFTC_ToyModel` inside  
   `scripts/gftc_core.py`.  
   Feel free to change lattice size, potentials, coupling forms, initial
   conditions, etc.

---

## 📈 Reproducible Results

| Figure | Description | Scientific Meaning |
|--------|-------------|--------------------|
| `figure1_phase_transition.png` | Order parameter vs. `λ_c` with sudden jump and peak in derivative.  Insets show `∇ × A` evolving from noise to clear vortices. | **First computational evidence** for a *critical coupling threshold* of consciousness. |
| `figure2_2d_phase_diagram.png` | Heat-map of order parameter in `(μ, λ_c)` plane displaying a *tilted boundary* and a high-order *plateau*. | Demonstrates that consciousness is a *synergistic product* of neural excitability and global integration—offers a **unified theoretical coordinate** for states such as anaesthesia, sleep, wakefulness. |

---

## 🔧 Model in a Nutshell

**Fields on a 2-D periodic lattice**  
- `Ψ` (complex scalar) – *neural activity field*  
- `φ` (real scalar) – *causal-density field* (bi-stable potential)  
- `A_μ = (Ax, Ay)` – *U(1) gauge field* whose curl represents the
  **geometric signature of consciousness**.

**Action (discretised)**  

S = ∫[ |Dψ|² + V_ψ(ψ) + ½(∇φ)² + V_φ(φ) + ¼ F_{μν}F^{μν}
     + λ_c φ |ψ|²  +  μ φ² ] d²x

with `D_μ = ∇_μ - i A_μ` and `F_{μν} = ∂_μ A_ν - ∂_ν A_μ`.

**Dynamics**  
Gradient-descent relaxation in fictitious time ⇨ system flows toward
**low-energy states**.  
Order parameter = **spatial standard deviation of `∇ × A`**.

---

## 🧠 Theoretical Background & Further Reading

GFTC attempts to bridge the *explanatory gap* in consciousness studies by
mapping:

- **qualia** → geometry of high-dimensional experience-space sections,  
- **unity of consciousness** → existence of global sections of a fibre bundle,  
- **mind–matter interaction** → gauge-invariant coupling term.

A formal derivation, philosophical motivation and comparison with Integrated
Information Theory (IIT) and other frameworks will be available in the
upcoming pre-print (link to be added).

---

## 🤝 Contributions Welcome

- Questions on assumptions, maths or philosophy?  
- Code optimisation, bug reports, new features?  
- Ideas for new simulations (attention switching, pathological states, …)?

Please open a **[GitHub Issue](https://github.com/YOUR_USERNAME/GFTC-Consciousness-Field-Theory/issues)** – we look forward to exploring the *geometry of consciousness* together!

---

## 📜 Citation & Licence

If you use this code or build on these ideas, please:

- Link to this repository.  
- Cite as:  
  *“GFTC (Geometric Field Theory of Consciousness) numerical toy model”*.

Released under the **MIT Licence** – feel free to use, modify and distribute,
but keep the original copyright notice.

---

**Explorer’s remark**:  
Consciousness may be the most complex phenomenon in the universe, yet it is
not an impenetrable mystery. This toy model is a rough but determined key to
the door of understanding—your help in refining it is warmly welcome!
```
