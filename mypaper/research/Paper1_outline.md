# Paper 1 — Time-averaged characterization

**Working title:** Lattice-Boltzmann simulation of cross-flow through ordered and disordered particle arrays: numerical framework, validation, and Reynolds-dependent flow regimes

**Scope:** Time-averaged / steady characterization. Methods + validation + Re–θ regime map + ordered-vs-disordered comparison from mean fields. All instantaneous / spectral / modal analyses are deferred to Paper 2.

**Target length:** ~14–18 pages, ~10 figures, 2 tables.

---

## 1. Strategic positioning

- This is the foundational paper of the series. It establishes the numerical framework, demonstrates validation across all geometries used in Paper 2, and reports the first new physics in the form of a Re–θ flow-regime map and an ordered-vs-disordered comparison.
- Validation is consolidated into one figure, not stretched across the paper.
- The "methods" emphasis is concrete and reviewer-defensible: collision operator, boundary scheme for oblique/curved interfaces, force evaluation, geometry generation for irregular packings.
- Paper 2 is forward-cited from §7 so reviewers see the series logic.

## 2. Headline novelty claims (write these into the abstract verbatim)

1. First systematic Re–θ flow-regime map for cross-flow through obliquely-stacked particle arrays, resolved at Re = 100, 300, 500 and θ = 30°, 40° (and ideally one intermediate angle).
2. Quantitative ordered-vs-disordered comparison of pressure drop, drag distribution, channeling, and permeability at matched bulk Re and mean porosity — a controlled disorder experiment not feasible with the experimental setup.
3. LBM (Alborz) validated against PIV across all geometries to within < 2.5 % average relative error in layer-wise velocity.

## 3. Section structure

### 1. Introduction (~1.5 pages)

- Motivation: packed beds in reacting particle systems (cite the Magdeburg workshop and the SPP context), oblique stacking in industrial fixed beds.
- State of the art:
  - Experimental work on Reference Configuration IIa (cite the two experimental papers and the workshop).
  - Prior LBM-on-packed-bed work (cite Hill, van der Hoef, Tenneti–Subramaniam style work).
  - Limited treatment of oblique stacking in the LBM literature.
- Gap: experiments are restricted in Re coverage, do not resolve pressure / per-particle drag, and sample only one realization of disorder.
- Contributions (3–4 bullets).
- Paper-2 forward pointer at the end of the intro.

### 2. Numerical method (~2.5 pages) — this is where the "methods" muscle lives

- 2.1 LBM formulation in Alborz (collision operator: BGK / MRT / regularized — be explicit; lattice DnQm; equilibrium form).
- 2.2 Boundary scheme for inclined curved particles (interpolated bounce-back or IBM; cite scheme used; justify choice for oblique stacks where naïve bounce-back is staircased).
- 2.3 Force and torque evaluation on particles (momentum-exchange or stress-integration).
- 2.4 Computational domain, inlet/outlet (Zou–He / equilibrium / convective outflow), lateral boundary conditions.
- 2.5 Geometry generation:
  - Regular 30° and 40° stacks: lattice spacing, particle diameter, number of layers.
  - Irregular configurations: disorder protocol (random perturbation of lattice nodes, MC packing, or other — describe explicitly and reproducibly). Report disorder metrics (local porosity PDF, nearest-neighbour PDF, orientation PDF) at the end of §2.5.
- 2.6 Computational cost (per case, MLUPS, parallel scaling — short).

### 3. Verification and validation (~2 pages)

- 3.1 Grid convergence: Richardson extrapolation or GCI on chosen QoI (ΔP or peak velocity at a fixed probe). One figure.
- 3.2 Time-step and Mach-number sensitivity (short).
- 3.3 Validation against PIV:
  - One composite figure with all geometries (regular 30°, 40°, irregular) on one page.
  - Quantitative error norms (L2 over PIV layers; % difference per layer).
  - Headline number: < 2.5 % mean relative error.

### 4. Mean-flow characterization in ordered arrays (~3 pages) — first slice of new physics

- 4.1 Velocity field and streamline patterns through the array, Re = 100, 300, 500 at 30° and 40°.
- 4.2 Penetration depth and length to fully-developed periodic flow (layer-wise convergence of profile shape).
- 4.3 Per-particle drag coefficient C_D vs layer index for each Re and θ. Identifies entrance-region effect and asymptotic value.
- 4.4 Pressure drop ΔP(Re, θ). Compare with modified Ergun-type correlation; report deviation factor and discuss applicability of standard correlations to oblique stacks.
- 4.5 Wall-shear distribution on representative particles.

### 5. Flow regimes and regime map (~2 pages) — the headline novelty

- 5.1 Regime criteria based on time-averaged signatures only (the unsteady criteria are in Paper 2):
  - R1: symmetric, attached (Re low).
  - R2: symmetric with recirculation pockets.
  - R3: asymmetric / lateral deflection in mean field.
  - R4: mean field shows separated wake structures consistent with downstream shedding (which Paper 2 quantifies).
- 5.2 Re–θ regime map (figure).
- 5.3 Transition Re as a function of θ.
- 5.4 Engineering implication: which regions of the map break the assumptions of standard packed-bed correlations.

### 6. Effect of disorder (~2 pages) — irregular cases folded in here

- 6.1 Recap of disorder protocol and statistical descriptors (forward from §2.5).
- 6.2 Mean-flow comparison: irregular vs the nearest regular case at matched bulk Re and matched mean porosity (or matched ΔP if you prefer to control on pressure drop — pick one and justify).
- 6.3 Channeling and dead-zone statistics from local velocity-magnitude PDFs (highlight tails).
- 6.4 ΔP and effective permeability: ordered vs disordered.
- 6.5 Tortuosity from streamline integration (cheap to add and reviewer-pleasing).
- 6.6 Per-particle drag distribution histogram: ordered (delta-like) vs disordered (broad).

### 7. Discussion (~1 page)

- Strengths and limits of the Alborz framework on this class of geometry.
- Implications for engineering correlations (Ergun-type) on oblique and disordered beds.
- Forward pointer to Paper 2: mean fields characterize regime *boundaries*, but the *mechanism* of unsteady transition (Strouhal, modes, wake interaction) is the subject of the companion paper.

### 8. Conclusions (~0.5 page)

3–4 bullets, each tied to a novelty claim in §2.

## 4. Figure list (10 figures)

| # | Figure | Content | Source |
|---|---|---|---|
| 1 | Geometry & setup | Schematic of 30°, 40°, irregular configurations with PIV-plane and probe locations; coordinate system | New |
| 2 | Numerical scheme | Boundary treatment near oblique particles + grid detail near interface; small inset of node layout | New |
| 3 | Grid convergence | QoI vs Δx (log-log) with Richardson fit; time-step independence inset | New |
| 4 | Validation composite | Side-by-side exp/sim velocity contours for all geometries on one figure; error % annotated | Adapted from existing surface and irregular comparisons |
| 5 | Layer velocity profiles | u(y) at layers 13–17 for one representative Re; sim/exp curves overlaid | Adapted from existing layer plot |
| 6 | Mean velocity & streamlines | Contour + streamlines for Re = 100, 300, 500 at 30° (and one row for 40°) | New |
| 7 | Drag & pressure | C_D per particle vs layer index (left panel); ΔP vs Re per θ (right panel) | New |
| 8 | Re–θ regime map | Symbols on Re vs θ axes; shaded regime regions; transition curve | New |
| 9 | Disorder statistics | PDFs of local porosity, NN distance, orientation for irregular case | New |
| 10 | Ordered vs disordered | Velocity PDF comparison; ΔP / permeability bar chart; drag distribution histogram | New |

## 5. Tables

- **Table 1:** Simulation matrix — Re × θ × geometry, mesh, Δt, runtime, MLUPS.
- **Table 2:** Validation error norms (L2 over PIV layers, max % deviation) per case.

## 6. What is explicitly NOT in Paper 1 (reserved for Paper 2)

- Strouhal numbers, frequency spectra.
- POD / DMD modal analysis.
- Wake-to-wake interaction maps.
- Vorticity transport budget.
- Pressure-fluctuation statistics (mean pressure stays in Paper 1).
- Lagrangian tracer / residence-time distributions (could optionally go in either; suggest Paper 2 because they leverage instantaneous fields).

## 7. Open decisions to make before drafting

1. Choose the LBM collision operator description (which Alborz actually uses) and the boundary scheme name — be ready to cite the original references.
2. Decide whether disorder is controlled by lattice-node perturbation or by independent packing generation; pick one and stick to it across §2.5, §6, and Paper 2.
3. Decide the matching criterion for ordered-vs-disordered comparison: matched bulk Re + matched mean porosity is the cleanest; matched ΔP is also defensible. Pick one and state it explicitly.
4. Confirm whether Re = 500 cases are complete for *all* angles before submission. Missing Re = 500 at one angle weakens the regime map.
5. Decide whether an intermediate angle (e.g. 35°) is added. Without it, the regime map has 2 angle columns only.

## 8. Suggested target journals (in rough preference order)

- *Journal of Fluid Mechanics* — if the regime map and disorder comparison are strong.
- *International Journal of Heat and Fluid Flow*.
- *Physics of Fluids*.
- *Computers & Fluids* — if reviewers want a stronger methods emphasis than physics emphasis.
- *Powder Technology* / *Particuology* — to stay in the experimental group's publication ecosystem (their Particuology paper is cited; this places the series adjacent).

## 9. Suggested abstract skeleton (~180 words, fill in numbers)

> Cross-flow through obliquely-stacked particle arrays underpins reacting particle systems and structured packed beds, yet the combined effect of inclination angle, Reynolds number, and packing disorder on the mean flow remains poorly characterised. We present a lattice-Boltzmann (Alborz) study of cross-flow through ordered (30°, 40°) and disordered particle arrays at Re = 100, 300, 500, validated against high-resolution PIV data from Reference Configuration IIa to within < 2.5 % mean relative error in layer-wise velocity. From the validated simulations we extract quantities inaccessible to experiment — per-particle drag, pressure drop, and wall shear — and construct the first Re–θ flow-regime map for this configuration, identifying the transition from attached symmetric flow to wake-dominated regimes. A controlled order-vs-disorder comparison at matched bulk Reynolds number and mean porosity quantifies the disorder-induced broadening of per-particle drag, the emergence of channeling, and the reduction of effective permeability. The results provide a quantitative benchmark for LBM in oblique particle arrays and constrain engineering correlations for non-axially aligned packings.
