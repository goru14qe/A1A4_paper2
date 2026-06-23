# Figures and content inherited from Velten et al. (2026)

**Reference:** Velten, C., Hülz, K., & Zähringer, K. (2026). Allowing optical measurements
in a 3D packed bed with gas flow: A novel reactor concept. *Particuology*, 108, 293–306.
https://doi.org/10.1016/j.partic.2025.11.018

**License:** Open Access, CC BY 4.0 — figures may be reproduced with attribution.

---

## Geometry parameters (Table for §2 / §3.3)

| Parameter | Symbol | Value | Source |
|---|---|---|---|
| Bar height (characteristic length) | l_ch | 10 mm | Fig. 2 / §3.1 |
| Slit width between bars | l_P | 5 mm | Fig. 2 |
| Column (inlet) diameter | d_inlet | 62.12 mm | Fig. 2 |
| Porosity | φ | 0.332 | §2.2 |
| Total number of layers | — | 18 (= 3 × 6-layer periods) | §3.1 |
| Rotation step resolution | — | 5° increments (37 rim slits) | §2.2 |
| Rotation angle studied | θ | 30° | §3.1 |
| Layers in measurement window | — | L13–L17 (third period) | §3.1 |
| Measurement positions (from centre) | a_Pos,n | Pos1: −22.5 mm, Pos3: −7.5 mm, Pos5: +7.5 mm, Pos7: +22.5 mm | Table 1 |
| Air density | ρ | 1.204 kg/m³ | §3.2 |
| Air dynamic viscosity | μ | 1.822 × 10⁻⁵ kg/(m·s) | §3.2 |
| Temperature / pressure | T, p | 20 °C, 1 atm | §3.2 |
| Volume flow rate at Re_p = 100 | Q | 9.14 l/min | §3.2 |
| Cross-sectional area | A | 3031 mm² | §3.2 |
| Re_p definition | Re_P | v_z · ρ · l_ch / (φ · μ) | Eq. (1) |

---

## Figures to use in Paper 1

| Christin Fig. | Content | Your paper section | Your figure | How to use |
|---|---|---|---|---|
| **Fig. 2** | Module top-view with all key dimensions (l_P = 5 mm, l_ch = 10 mm, d_inlet = 62.12 mm), rotation-slit detail, complete modular stack | §2 Geometry | **Fig. 1** panel | Reproduce with attribution; shows all geometry specs in one panel |
| **Fig. 5** | Layers 13–18 with 30° rotation increments labelled, Pos 1/3/5/7 marked on surface layer, 3D spiral-stack render | §2 Geometry / §3.6 | **Fig. 1** or **Fig. 2** panel | Directly illustrates the twist-and-repeat structure and measurement window |
| **Fig. 3** | How rotation angle controls pore-inlet count between adjacent layers (0°→90°) | §2 Geometry | **Fig. 1** panel (optional) | Supports the twist-and-repeat framing in the text |
| **Fig. 6** | Global (x, y, z) vs in-plane (ξ, z) coordinate system for 0° and −30° layers | §3.6 Comparison methodology | **Fig. 2** panel | Explains the coordinate transformation between PIV frame and simulation frame |
| **Fig. 10** (Re_p = 100 rows only) | Averaged \|V\| colour fields + streamlines for L13–L17, Pos 1; line profiles at Δz = 1, 5, 9 mm | §3.7 Validation / §4 | **Fig. 5** (experiment panels) | Use as the PIV reference panels in the side-by-side LBM vs PIV layer validation |
| **Fig. 11** (Re_p = 100 rows only) | Same as Fig. 10 for Pos 3 | §3.7 Validation | **Fig. 5** (experiment panels) | Second measurement position in layer validation |
| **Fig. 8** (Re_p = 100 rows only) | Mean surface fields Pos 1 & Pos 7 at Re_p = 100; point-symmetry line profiles at z = 182, 205, 235 mm | §3.7 Validation | **Fig. 4** (experiment panels) | Use as PIV reference for surface-level comparison |
| **Fig. 9** (Re_p = 100 rows only) | Mean surface fields Pos 3 & Pos 5 at Re_p = 100 | §3.7 Validation | **Fig. 4** (experiment panels) | Second set of positions in surface validation |

---

## Figures NOT to use in Paper 1

| Christin Fig. | Reason |
|---|---|
| Fig. 7 (PIV lab photo) | Equipment photograph — not standard in numerical papers; cite the paper instead |
| Fig. 12 (instantaneous snapshots, Re_p = 1000) | Time-resolved data — Paper 2 territory |
| Fig. 13 (TKE, Re_p = 1000) | Turbulence statistics at high Re — Paper 2 territory |
| Re_p = 1000 panels in Figs 8–11 | No matched high-Re LBM data in Paper 1 |
| Fig. 4 (side-jet module) | Not relevant to the standard configuration studied |

---

## Draft text for §2 (Geometry & Benchmark) citing these figures

The experimental reference configuration is described in detail by \citet{velten2026}.
The packing consists of polyhedral bar modules, each containing five parallel bars of
height $l_\mathrm{ch} = 10\,\mathrm{mm}$ separated by slits of width $l_P = 5\,\mathrm{mm}$,
housed within a circular cross-section of diameter $d_\mathrm{inlet} = 62.12\,\mathrm{mm}$
(Fig.~\ref{fig:geometry}, reproduced from \citealt{velten2026}).
The void volume fraction (porosity) is $\varphi = 0.332$.
Modules are stacked in sets of 18 layers; each module can be rotated against its
neighbour in increments of $5^\circ$ via 37 indexing slits on the rim
(\citealt{velten2026}, Fig.~2).

For the regular 30° configuration studied here, each successive layer is rotated by
$\theta = 30^\circ$, generating a helical superlattice with a geometric period of
$N = 180^\circ / \theta = 6$ layers (since the bar pattern is $180^\circ$-symmetric).
The 18-layer bed therefore contains exactly three complete periods.
The top six layers (L13–L17) correspond to the third period and are the primary
comparison window, matching the PIV measurement layers of \citet{velten2026}
(their Fig.~5, reproduced here as Fig.~\ref{fig:layers}).

The in-plane coordinate system follows \citet{velten2026}: the horizontal in-plane
coordinate $\xi$ originates at the centre of the void at the measurement position,
and the streamwise coordinate $z$ originates at the bottom of the first (lowest)
module (Fig.~\ref{fig:coords}, after \citealt{velten2026} Fig.~6).
Measurement positions Pos~1, 3, 5, 7 are located at
$a_{\mathrm{Pos}} = -22.5,\,-7.5,\,+7.5,\,+22.5\,\mathrm{mm}$ from the reactor
centre, respectively (Table~1 of \citealt{velten2026}).

The particle Reynolds number is defined as
\begin{equation}
    Re_P = \frac{v_z \, \rho \, l_\mathrm{ch}}{\varphi \, \mu},
\end{equation}
where $v_z$ is the superficial velocity, $\rho = 1.204\,\mathrm{kg/m^3}$ and
$\mu = 1.822 \times 10^{-5}\,\mathrm{kg/(m\,s)}$ are the density and dynamic viscosity
of air at $T = 20\,^\circ\mathrm{C}$ and $p = 1\,\mathrm{atm}$
\citep{velten2026}.
The present study covers $Re_P = 100$ for all three topologies (30°, 40°, irregular)
and additionally $Re_P = 300$ and $500$ for the 40° configuration.

---

## Draft text for §3.6 (Experimental–Numerical Comparison Methodology) citing these figures

Velocity data are reported in the in-plane coordinate system of
\citet{velten2026} (their Fig.~6): the horizontal in-plane axis $\xi$ and the
vertical streamwise axis $z$.
Simulation planes are extracted at the physical $y$-positions corresponding to
Pos~1 and Pos~3 ($a_{\mathrm{Pos}} = -22.5$ and $-7.5\,\mathrm{mm}$
from the reactor centre), and at the streamwise heights of layers L13–L17,
matching the PIV measurement layers of \citet{velten2026}.
Each extracted plane is masked to the fluid region, interpolated onto the
experimental PIV grid (vector resolution $3.40$–$3.44\,\mathrm{vec/mm}$,
Table~2 of \citealt{velten2026}), and normalised by the local intrinsic mean
velocity $v_\mathrm{int} = v_z / \varphi$.

---

## BibTeX entry

```bibtex
@article{velten2026,
  author    = {Velten, Christin and H{\"u}lz, Kerstin and Z{\"a}hringer, Katharina},
  title     = {Allowing optical measurements in a {3D} packed bed with gas flow:
               {A} novel reactor concept},
  journal   = {Particuology},
  volume    = {108},
  pages     = {293--306},
  year      = {2026},
  doi       = {10.1016/j.partic.2025.11.018},
  note      = {Open Access, CC BY 4.0}
}
```
