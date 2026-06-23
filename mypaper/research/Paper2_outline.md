# Paper 2 — Time-resolved unsteady dynamics

**Working title:** Unsteady wake dynamics and coherent structures in ordered and disordered particle arrays: a time-resolved lattice-Boltzmann study

**Scope:** Instantaneous and modal analysis of the same simulation database used in Paper 1. Strouhal scaling, vortex shedding, wake interaction across layers, POD / DMD modal decomposition, and pressure-fluctuation statistics. Validation and mean-flow context are *cited* from Paper 1, not repeated.

**Target length:** ~12–16 pages, 8–10 figures, 1–2 tables.

---

## 1. Strategic positioning

- Paper 2 is the physics companion to Paper 1. The simulation set is the same; the analysis is entirely on instantaneous snapshots.
- The "uses data you already have" argument is real: every figure here is a post-processing step on stored flow fields. No new simulations are required unless Re = 500 cases are incomplete.
- Novelty rests on quantities the experimental group did not (and largely cannot) extract: pressure fluctuations, time-resolved 3D coherent structures, modal frequencies, vorticity-transport budgets.

## 2. Headline novelty claims

1. First spectral and modal characterisation of unsteady flow through obliquely-stacked particle arrays, covering ordered (30°, 40°) and disordered configurations under matched bulk conditions.
2. Strouhal–Re–θ scaling for the dominant shedding frequency, including the layer at which periodic shedding locks in.
3. POD / DMD modal decomposition that identifies inter-layer wake-coupling modes and contrasts coherent-structure topology between ordered and disordered beds.
4. Quantification of pressure-fluctuation intensity within the array — a quantity directly inaccessible to PIV.

## 3. Section structure

### 1. Introduction (~1 page)

- Brief recap of the configuration and motivation; cite Paper 1 for full setup.
- State of the art on unsteady wake dynamics in particle arrays (single-cylinder shedding, cylinder pairs / tandem, then move to multi-row arrays). Cite classic Strouhal–Re work and prior POD/DMD on bluff-body wakes.
- Gap: no time-resolved modal analysis exists for oblique multi-layer arrays; experimental PIV time resolution rarely reaches shedding frequencies in this geometry; pressure fluctuations are unmeasured.
- Contributions (3–4 bullets matching §2 above).

### 2. Database and post-processing methods (~1.5 pages)

- 2.1 Simulation database (one paragraph + table): cases reused from Paper 1, sampling rate, total run length, statistical stationarity check.
- 2.2 Probe network: positions chosen to cover entrance, developed, and exit regions of the array, plus inter-particle gaps.
- 2.3 Spectral analysis (Welch, windowing, frequency resolution, normalisation to Strouhal number St = f·d/U).
- 2.4 POD (snapshot method): number of snapshots, energy convergence, mode ordering.
- 2.5 DMD: algorithm variant used (exact DMD / TDMD / sparsity-promoting DMD), rank truncation, mode-amplitude criterion.
- 2.6 Vorticity-transport budget: terms computed, integration volumes.

### 3. Onset and character of unsteadiness (~2 pages)

- 3.1 Time histories at representative probes for Re = 100, 300, 500 across θ = 30°, 40° and irregular case; visual classification (steady, periodic, quasi-periodic, chaotic).
- 3.2 Spectral signatures (PSDs at the same probes).
- 3.3 Refined regime boundaries on the Re–θ map from Paper 1 — now sharpened by unsteady criteria. Show how the time-averaged classification of Paper 1 over- or under-estimates the true onset of unsteadiness.

### 4. Strouhal scaling and lock-in (~2 pages)

- 4.1 Dominant frequency vs Re per θ; collapse on St(Re, θ).
- 4.2 Layer at which periodic shedding locks in (definition: layer index beyond which the dominant PSD peak narrows below a chosen bandwidth threshold).
- 4.3 Comparison with single-cylinder and tandem-cylinder reference values; quantify suppression or enhancement of shedding by array confinement.
- 4.4 Irregular case: distribution of local shedding frequencies (multiple peaks); contrast with the sharp peaks of ordered cases.

### 5. Coherent structures: POD and DMD (~3 pages) — analytical centrepiece

- 5.1 POD energy spectrum across cases. Identify the number of modes carrying, e.g., 80 % of the kinetic energy.
- 5.2 Spatial structure of leading POD modes for one representative ordered case (e.g. 30°, Re = 300). Identify mode pairs corresponding to convective shedding.
- 5.3 DMD spectrum (frequency vs amplitude vs growth rate). Identify physically dominant modes (high amplitude + near-neutral growth) and tie their frequencies back to the Strouhal scaling of §4.
- 5.4 Inter-layer coupling: cross-correlation / phase-locking analysis between probes across layers; quantify the spatial coherence length of the dominant mode.
- 5.5 Ordered vs disordered: same POD/DMD analysis on the irregular case; compare mode topology, dimensionality (number of modes for fixed energy fraction), and coherence length.

### 6. Pressure-fluctuation statistics and vorticity transport (~1.5 pages)

- 6.1 RMS pressure fluctuation field; spatial distribution of high-p' regions tied to wake impingement zones.
- 6.2 Frequency content of pressure fluctuations at particle surfaces (mechanical-loading implication).
- 6.3 Vorticity-transport budget along a streamwise slab through the array: relative magnitude of convection, stretching, viscous diffusion. Identify which mechanism dominates the layer-to-layer propagation of unsteadiness.

### 7. Discussion (~1 page)

- Mechanism of unsteady transition: locally driven by individual wakes vs globally driven by inter-layer coupling.
- How disorder modifies coherent-structure formation (broadens, fragments, or suppresses).
- Practical implications: mechanical loading, mixing, mass/heat-transfer relevance.
- Limits of the analysis (statistical convergence, Re range, single irregular realisation if applicable).

### 8. Conclusions (~0.5 page)

3–4 bullets aligned with the novelty claims in §2.

## 4. Figure list (9 figures)

| # | Figure | Content | Source |
|---|---|---|---|
| 1 | Probe network & sampling schematic | Geometry with probe locations and PIV-plane indication; sketch of sampling window | New |
| 2 | Time histories | u'(t) at three representative probes for Re = 100, 300, 500 across cases; vertical layout | New |
| 3 | PSD overview | log-log PSDs at the developed-region probe for all cases on one figure (colour by Re, line style by geometry) | New |
| 4 | Refined regime map | Re–θ map from Paper 1 with unsteady onset overlaid; symbols indicate periodic / quasi-periodic / chaotic | Adapted from Paper 1 figure |
| 5 | Strouhal scaling | St(Re) for each θ and irregular case; reference lines for single-cylinder and tandem | New |
| 6 | POD modes | Energy spectrum (left) + spatial structure of leading two mode pairs (right grid) for one representative case | New |
| 7 | DMD spectrum & modes | Frequency–amplitude–growth scatter (left) + spatial structure of two dominant DMD modes (right) | New |
| 8 | Ordered vs disordered modal comparison | POD/DMD modal energy distribution and coherent-structure topology, ordered vs irregular | New |
| 9 | Pressure fluctuations & vorticity budget | RMS p' contour (left) + vorticity-transport budget along streamwise direction (right) | New |

## 5. Tables

- **Table 1:** Simulation database — cases, sampling rate, record length, number of snapshots used for POD/DMD.
- **Table 2:** Dominant Strouhal numbers and modal energy fractions by case (compact summary).

## 6. What is deliberately NOT in Paper 2

- Validation figures (cite Paper 1).
- Mean-flow contour plots (cite Paper 1).
- Ergun-type pressure-drop discussion (cite Paper 1).
- Steady-regime classification (cite Paper 1).
- Per-particle mean drag (Paper 1); per-particle drag *fluctuation* statistics belong here only if they carry a clean physics message.

## 7. Cross-references between Paper 1 and Paper 2

- Paper 2 §1 cites Paper 1 for the configuration, geometry, and validation.
- Paper 2 §3.3 explicitly compares its refined regime boundaries against the time-averaged map in Paper 1 §5.2.
- Paper 1 §7 contains a forward pointer to Paper 2 stating that mean fields delineate regime *boundaries* but the *mechanism* is the subject of Paper 2.
- Avoid repeating figures: validation, mean velocity contours, mean drag, Re–θ map (Paper 1 version) appear in Paper 1 only; the *refined* Re–θ map with unsteady overlay appears only in Paper 2.

## 8. Open decisions before drafting

1. Confirm sampling rate of stored instantaneous data: is it sufficient to resolve the expected Strouhal frequencies at Re = 500? Rule of thumb: at least 10 samples per shedding period; record length covering ≥ 50 periods.
2. Choose DMD variant. For these flows, sparsity-promoting DMD or exact DMD with energy-based truncation is usually sufficient. State the rank explicitly.
3. Decide whether POD is done on velocity, vorticity, or pressure. Velocity is conventional; vorticity sharpens wake structure; pressure highlights acoustic-like modes if present.
4. Decide irregular-case sample size for modal analysis: a single realisation is adequate for a first analysis but should be acknowledged as a limit.
5. Decide if a Lagrangian / residence-time-distribution section is added (one extra figure). It would broaden engineering relevance (mixing / mass transfer) but lengthens the paper.

## 9. Suggested target journals (in rough preference order)

- *Journal of Fluid Mechanics* — modal / coherent-structure papers fit naturally here.
- *Physics of Fluids* — fast track on POD/DMD-driven analyses.
- *International Journal of Heat and Fluid Flow*.
- *Flow, Turbulence and Combustion* — if the unsteady-transport / mixing angle is emphasised.

## 10. Suggested abstract skeleton (~180 words, fill in numbers)

> Unsteady flow through obliquely-stacked particle arrays controls the mechanical loading, mixing, and transfer characteristics of structured packed beds, yet its modal and spectral character is largely uncharted. Using a validated lattice-Boltzmann (Alborz) database covering Re = 100, 300, 500 across ordered (30°, 40°) and disordered particle arrangements [companion paper], we extract the time-resolved dynamics of cross-flow through these arrays. Spectral analysis reveals a Strouhal scaling St(Re, θ) that departs measurably from the single-cylinder reference and identifies the array layer at which periodic shedding locks in. Proper orthogonal and dynamic mode decompositions expose inter-layer wake-coupling modes whose spatial coherence length contracts with disorder and whose modal dimensionality grows with Reynolds number. Pressure-fluctuation fields — inaccessible to PIV — concentrate at wake-impingement sites and govern the layer-to-layer propagation of unsteadiness, as confirmed by a vorticity-transport budget. The results provide the first modal-level description of unsteady cross-flow through obliquely-stacked particle arrays and quantify the role of geometric disorder in fragmenting otherwise coherent shedding.
