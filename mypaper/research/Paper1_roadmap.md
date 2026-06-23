# Paper 1 — Combined Roadmap

Merges the structure of *Paper 1 Outline.pdf* (your draft) with the novelty / cross-paper logic of *Paper1_outline.md*. Adopts your stronger framing ("rotational pore topology + Re-dependent instability + coherent flow organization") and your four-tier validation strategy. Adds explicit novelty claims, a Re–θ regime map, per-particle drag, Ergun comparison, and a matched-condition ordered-vs-disordered comparison.

---

## 0. Critical decision: architecture variant

Your PDF includes FFT/probes (§4.3) and Q/λ2 vortex analysis (§4.5) — both rely on instantaneous data and were Paper 2 in the agreed 2-paper split. Two viable architectures:

### Variant A — Lean Paper 1, rich Paper 2 (recommended)

Paper 1 stays **strictly time-averaged**. FFT, instantaneous Q/λ2, POD/DMD, pressure fluctuations all move to Paper 2.

- Pros: clean 2-paper differentiation, each paper has a sharp thesis, no overlap.
- Cons: Paper 1 loses some of the "wow factor" visuals that instantaneous fields give.

### Variant B — Comprehensive Paper 1, focused Paper 2

Paper 1 covers everything in your PDF outline (including FFT and vortex on time-averaged + instantaneous). Paper 2 narrows to a focused contribution: POD/DMD modal decomposition + pressure-fluctuation statistics + inter-layer wake coupling.

- Pros: Paper 1 matches your PDF draft as-is; reviewers see a complete picture.
- Cons: harder to justify Paper 2 as standalone; risk of reviewer saying "this should have been one paper."

**Recommendation: Variant A.** The 2-paper split is only defensible if the split is *clean*. Time-averaged vs time-resolved is the cleanest possible cut. Variant B forces Paper 2 to be a narrow methods paper which is harder to land in good journals.

The rest of this roadmap follows **Variant A**. Switch to Variant B by un-deferring §4.3 and §4.5 and trimming Paper 2 accordingly.

---

## 1. Integrated Paper 1 structure (Variant A)

### Title (working)

*Rotational pore topology and Reynolds-dependent flow organization in structured packed porous beds: a validated lattice-Boltzmann study*

### Hook sentence (for abstract opener)

> The interaction between rotational pore topology, Reynolds-number-dependent flow organization, and packing disorder in structured porous beds remains insufficiently quantified at the pore scale.

### Explicit novelty claims (write these in §1.4 and abstract)

1. First pore-resolved, three-dimensional LBM characterisation of cross-flow through rotationally-stacked particle arrays validated against PIV across four tiers (global, local, statistical, structural) with mean relative error < 2.5 % in layer-wise velocity.
2. First systematic Re–θ map of mean-flow organisation regimes for this configuration, spanning Re = 100, 300, 500 at θ = 30°, 40° (and irregular).
3. First quantitative ordered-vs-disordered comparison at matched bulk Reynolds number and matched mean porosity, isolating the effect of topological irregularity from confounding bulk effects.
4. Extraction of quantities inaccessible to PIV (per-particle drag distribution, pore-scale pressure drop, wall shear, tortuosity) and their use to test Ergun-type correlations for non-axially aligned packings.

### Section structure

#### 1. Introduction (~1.5 pages)

- 1.1 Packed porous media and transport limitations *(from your PDF — keep)*
- 1.2 Limitations of Darcy / Ergun and the case for pore-scale resolution *(from your PDF — keep)*
- 1.3 Rotational pore topology: concept, periodicity, alignment length, regular vs irregular *(from your PDF — keep, this is the strongest framing)*
- 1.4 Literature gap and objectives *(rewrite as the four novelty claims above)*
- 1.5 Paper-2 forward pointer *(one sentence)*

#### 2. Experimental and numerical methodology (~3 pages)

- 2.1 Experimental setup (PIV summary; brief — cite the experimental papers for full detail)
- 2.2 Geometry / topology definition (rotational increment, periodicity, alignment length; regular 30°/40°, irregular)
- 2.3 LBM methodology in Alborz (D3Q19 or D3Q27 — state which; collision operator; forcing; boundary conditions on inclined curved interfaces)
- 2.4 Numerical convergence (grid + time independence)
- 2.5 Experimental-to-numerical comparison methodology *(KEEP — this is one of your strongest sections)*
  - Plane extraction from 3D simulation to match 2D PIV planes
  - Coordinate transformation between PIV and simulation frames
  - Time-averaging procedure (stationarity window, sample count)
  - Spatial-projection / interpolation onto the PIV grid

#### 3. Validation strategy (~3 pages) — your four-tier scheme, expanded

- 3.1 Global validation: mean velocity, max velocity, flow-rate consistency, **density-based ΔP surrogate** (LBM-native: ρ_in − ρ_out)
- 3.2 Local validation: velocity profiles at PIV layers 13–17, jet locations, recirculation regions, contour overlays
- 3.3 Statistical validation: RMSE, normalised error, Pearson correlation, *(defer TKE and fluctuation intensity to Paper 2 since they require time-resolved data)*
- 3.4 Structural / topological validation: streamline organisation, coherent jet paths, mean recirculation topology agreement
- Headline number: **< 2.5 % mean relative error in layer-wise velocity** across all geometries.

#### 4. Results and discussion (~5 pages)

- 4.1 Mean-flow organisation in periodic rotational geometries *(from your PDF — extended)*
  - Jet formation and streamline locking
  - Coherent transport channels
  - Mean recirculation pockets
  - 30° vs 40° comparison
  - Penetration depth and length to fully-developed periodic flow
- 4.2 Reynolds-number dependence of mean-flow organisation *(was "transition" in your PDF — rename: instability transition itself is Paper 2)*
  - Mean-field signatures at Re = 100, 300, 500
  - Symmetry-breaking criterion in the *mean* field (not instantaneous)
  - Onset of mean-flow asymmetry as a function of Re, θ
- 4.3 **Re–θ flow-regime map** *(NEW — packaged figure)*
  - R1 attached symmetric, R2 symmetric with recirculation, R3 asymmetric mean, R4 mean field shows separated wakes
  - Map figure with regime boundaries
  - Engineering implication: which regions invalidate standard packed-bed correlations
- 4.4 Per-particle drag and pressure drop *(NEW — the "inaccessible to experiment" payload)*
  - C_D per particle vs layer index per Re per θ
  - ΔP(Re, θ) comparison with modified Ergun
  - Wall-shear distribution on representative particles
- 4.5 Effect of topological irregularity *(refactored from your §4.4 — controlled comparison)*
  - Disorder statistical descriptors (local porosity, NN distance, orientation PDFs)
  - **Matched-condition comparison**: irregular vs nearest regular case at matched bulk Re *and* matched mean porosity. State matching criterion explicitly.
  - Channeling and dead-zone statistics from local velocity-magnitude PDFs
  - Effective permeability and tortuosity from streamline integration
  - Per-particle drag distribution histogram: ordered (delta-like) vs disordered (broad)
- 4.6 Implications for transport and reactor design *(from your PDF — keep, tighten)*
  - Mixing implication based on tortuosity + channeling
  - Residence-time argument from mean field (full RTD goes to Paper 2 if Lagrangian tracking is added)
  - Flow homogenisation
  - Reactive-transport relevance — keep brief; do not promise heat / mass transfer simulations that aren't in this paper

#### 5. Conclusions (~0.5 page)

3–4 bullets, each tied directly to a numbered novelty claim from §1.4.

#### Forward pointer to Paper 2 (one paragraph at end of §5)

Mean fields characterise regime *boundaries*; the *mechanism* of unsteady transition (Strouhal scaling, modal structure, inter-layer wake coupling, pressure-fluctuation statistics) is the subject of the companion paper.

---

## 2. Sections deferred to Paper 2 (DO NOT include in Paper 1)

From your PDF outline, the following are moved to Paper 2 under Variant A:

- §3.3 statistical validation: TKE, fluctuation intensity (need time-resolved data; this is Paper 2's domain).
- §3.4 structural validation: *instantaneous* vortex / streamline agreement (Paper 1 keeps only mean streamlines and mean recirculation topology).
- §4.3 Temporal and fluctuation analysis (probes, FFT, oscillation frequencies, dominant modes).
- §4.5 Coherent structure and vortex analysis (Q, λ2, swirling) on *instantaneous* fields.
- Inter-layer wake coupling, POD / DMD, pressure-fluctuation statistics, vorticity-transport budget — all Paper 2.

---

## 3. Integrated figure list (10 figures)

| # | Figure | Content | Source / status |
|---|---|---|---|
| 1 | Geometry and topology | 30°, 40°, irregular configurations + rotation definition + alignment length; PIV plane and probe locations | New schematic |
| 2 | Experimental + numerical setup | PIV diagram (compact) + LBM domain + comparison-plane extraction methodology | Mostly new |
| 3 | Numerical scheme & convergence | Boundary treatment near oblique particles; grid-independence plot; time-step independence inset | New |
| 4 | Validation — global & local composite | Global table inset + side-by-side exp/sim velocity contours for all geometries; error % annotated | Adapted from existing surface and irregular plots |
| 5 | Validation — layer profiles + statistical metrics | u(y) at layers 13–17 (exp/sim overlay) + RMSE / Pearson / normalised-error bar charts | Adapted from existing layer_plots |
| 6 | Mean flow organisation, 30° | Mean velocity contours + streamlines for Re = 100, 300, 500 | New |
| 7 | Mean flow organisation, 40° + Re-dependence | Same for 40°; symmetry-breaking marker | New |
| 8 | Re–θ regime map | Symbols on Re vs θ axes; shaded regime regions; transition curve | New |
| 9 | Drag and pressure | C_D per particle vs layer index (left) + ΔP vs Re per θ with Ergun overlay (right) | New |
| 10 | Effect of irregularity (matched-condition) | Disorder statistics inset + velocity PDF comparison + permeability / tortuosity / drag-distribution comparison | New |

If forced to drop one figure, drop Figure 7 and merge into Figure 6 (single-figure 30° + 40°).

---

## 4. Tables

- **Table 1:** Simulation matrix — Re × θ × geometry, lattice (D3Q19/D3Q27), grid, Δt, runtime, MLUPS.
- **Table 2:** Four-tier validation summary — RMSE, Pearson, normalised error per case (compact, all cases on one table).

---

## 5. Data extraction checklist (what to compute from existing data)

Status: ✓ already have, ⚠ partially / needs work, ☐ to be done.

Time-averaged data (Paper 1 only):

- ✓ Mean velocity fields (3D), all cases
- ✓ Streamlines, all cases
- ✓ Velocity profiles at PIV layers
- ⚠ Density difference ρ_in − ρ_out → derive ΔP per case
- ☐ Per-particle drag coefficient C_D — integrate stress over particle surfaces
- ☐ Wall-shear distribution on representative particles
- ☐ Permeability — from ΔP and bulk velocity (Darcy fit)
- ☐ Tortuosity — from streamline integration
- ☐ Local porosity PDF, NN-distance PDF, orientation PDF for irregular case
- ☐ Channeling / dead-zone statistics — local velocity-magnitude PDFs
- ☐ Matched-condition selection — pick the regular case that best matches the irregular case's mean porosity

Validation post-processing:

- ⚠ Coordinate transformation between PIV and LBM frames (verify alignment)
- ⚠ Plane-extraction code from 3D LBM to 2D PIV plane (verify)
- ☐ Per-layer RMSE, normalised error, Pearson correlation
- ☐ Composite four-tier validation figure assembly

Method-section content:

- ☐ Decide and state explicitly: D3Q19 vs D3Q27
- ☐ Decide and state explicitly: collision operator (BGK, MRT, regularised, cumulant)
- ☐ Decide and state explicitly: boundary scheme for curved interfaces (interpolated bounce-back / IBM / cut-cell)
- ☐ Disorder protocol description (lattice-node perturbation vs Monte-Carlo packing vs other)
- ☐ Grid-independence study (if not yet at 3 grid levels, may need additional run)

---

## 6. Open decisions (must close before drafting)

1. **Architecture variant**: A (recommended, lean Paper 1) or B (comprehensive Paper 1, narrower Paper 2). Default in this roadmap: A.
2. **Lattice**: D3Q19 vs D3Q27 — state which Alborz uses for these runs.
3. **Collision operator** name and citation.
4. **Boundary scheme** name and citation for curved oblique interfaces.
5. **Disorder protocol** — single defensible recipe to be used in §2.2 and §4.5 and Paper 2.
6. **Matching criterion** for ordered-vs-disordered comparison: matched bulk Re + matched mean porosity (recommended) vs matched ΔP. Pick one.
7. **Re = 500 completion** — confirm runs are done for *all* geometries needed for the regime map. If any are missing, identify them now.
8. **Intermediate angle** (e.g. 35°) — add or not? Without it, the regime map has only two angle columns. Recommend adding one if compute budget allows.
9. **3D vs 2D for the simulation** — your PDF mentions D3Q19/D3Q27 (3D). Confirm; if 3D, the cross-plane comparison with 2D PIV must be addressed in §2.5 (which it now is).

---

## 7. Timeline / phases

### Phase 1 — Lock decisions (week 1)
- Close all nine open decisions in §6 above.
- Confirm completeness of simulation matrix; identify missing runs.

### Phase 2 — Post-processing (weeks 2–4)
- Implement / verify drag extraction (stress integration).
- Compute ΔP from density field for all cases.
- Compute permeability, tortuosity, channeling statistics.
- Compute disorder statistical descriptors.
- Implement coordinate-transformation and plane-extraction pipeline (or audit existing).

### Phase 3 — Validation pass (weeks 4–5)
- Generate four-tier validation outputs (global, local, statistical, structural).
- Assemble validation composite figures.

### Phase 4 — Regime classification (week 5)
- Apply mean-field regime criteria to each case.
- Build Re–θ regime map.

### Phase 5 — Figures and tables (weeks 5–6)
- Produce all 10 figures and 2 tables.

### Phase 6 — Drafting (weeks 6–8)
- Draft in order: §2 (method) → §3 (validation) → §4 (results) → §5 (conclusions) → §1 (intro, last). Abstract last.

### Phase 7 — Internal review and submission (week 9+)
- Co-author review, experimental-group review (they should review the validation section), submission.

In parallel with Phases 2–5, **start Paper 2 post-processing**: FFT, POD, DMD pipelines can be coded in parallel since they use the same simulation files. Drafting Paper 2 starts when Paper 1 is in internal review.

---

## 8. Suggested target journals (Paper 1)

- *Journal of Fluid Mechanics* — if novelty claims 2 and 3 land cleanly.
- *International Journal of Heat and Fluid Flow*.
- *Physics of Fluids*.
- *Chemical Engineering Science* — strong fit because §4.6 emphasises reactor implications.
- *Particuology* — adjacent to the experimental group's publication ecosystem.
- *Computers & Fluids* — if a methods reviewer pushes back and the methodological framing of §2 / §3 dominates.

---

## 9. Suggested abstract (~190 words, fill in numbers)

> The interaction between rotational pore topology, Reynolds-number-dependent flow organisation, and packing disorder in structured porous beds remains insufficiently quantified at the pore scale. We present a three-dimensional lattice-Boltzmann (Alborz) study of cross-flow through rotationally-stacked particle arrays at Re = 100, 300, 500 for inclination angles θ = 30°, 40° and for an irregularly-arranged configuration, all corresponding to Reference Configuration IIa. The simulations are validated against high-resolution PIV across a four-tier framework — global, local, statistical, and structural — with mean relative error below 2.5 % in layer-wise velocity. From the validated database we extract quantities inaccessible to experiment, including per-particle drag, pore-scale pressure drop, and wall-shear distributions, and use these to construct the first Re–θ map of mean-flow organisation regimes for this configuration. A controlled comparison between ordered and irregular packings at matched bulk Reynolds number and matched mean porosity isolates the effect of topological irregularity, quantifying the broadening of per-particle drag, the emergence of channeling, and the reduction of effective permeability. The results define the operating regimes in which standard Ergun-type correlations remain applicable and motivate the time-resolved analysis presented in the companion paper.
