#!/usr/bin/env python3
"""
Turbulent-kinetic-energy analysis for the flow-locking study.

Produces the two TKE figures used in the Flow Locking Framework section:

  fig_tke_perlayer_<TOPO>.png   per-layer k / k_mean for Re_P = 100 and 300
  fig_tke_field_<TOPO>.png      resolved k field of a representative layer,
                                Re_P = 100 (left) vs Re_P = 300 (right)

TKE is built from the diagonal Reynolds-stress components stored in the
transformed CSVs:  Re_tensor_0 = <u'u'>, Re_tensor_1 = <v'v'>, Re_tensor_2 = <w'w'>,
so that   k = 1/2 (<u'u'> + <v'v'> + <w'w'>).
The mean-flow kinetic energy is  k_mean = 1/2 |U|^2  from av_u_0, av_u_1, av_u_2.

The in-plane axes are Points_0 (horizontal in-plane, xi) and Points_2 (vertical z');
Points_1 is the constant out-of-plane depth of the Pos3 measurement plane.

Edit the CONFIG block to switch topology / positions / directories.
"""

import re
import glob
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# ----------------------------------------------------------------------
# CONFIG
# ----------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parents[2]      # .../A4-A1_2
TOPO      = "40"                                       # topology label used in output names
POS       = "Pos3"

# Data directories per Reynolds number (relative to the repository root).
RUN_DIRS = {
    100: REPO_ROOT / "40" / "sim" / "40_Re_100" / "Pos3_transformed",
    300: REPO_ROOT / "40" / "sim" / "40_Re_300" / "Pos3_transformed",
}

FIELD_LAYER = 15          # representative layer for the k-field figure (must exist in both runs)
OUTDIR      = REPO_ROOT / "mypaper" / "images"

# ----------------------------------------------------------------------
# IO helpers
# ----------------------------------------------------------------------
_LAYER_RE = re.compile(r"_L(\d+)_", re.IGNORECASE)


def layer_number(path: Path) -> int:
    m = _LAYER_RE.search(path.name)
    if not m:
        raise ValueError(f"cannot parse layer index from {path.name}")
    return int(m.group(1))


def load_layers(directory: Path) -> dict[int, pd.DataFrame]:
    """Return {layer_index: dataframe} for the base transformed CSVs (no *_flipped)."""
    files = [
        Path(f) for f in glob.glob(str(directory / "SIM_L*_T_transformed.csv"))
        if "flipped" not in Path(f).name
    ]
    if not files:
        raise FileNotFoundError(f"no transformed CSVs found in {directory}")
    return {layer_number(f): pd.read_csv(f) for f in sorted(files, key=layer_number)}


def tke(df: pd.DataFrame) -> pd.Series:
    """Resolved turbulent kinetic energy k = 1/2 (uu + vv + ww) [m^2/s^2]."""
    return 0.5 * (df["Re_tensor_0"] + df["Re_tensor_1"] + df["Re_tensor_2"])


def mean_flow_ke(df: pd.DataFrame) -> pd.Series:
    """Mean-flow kinetic energy k_mean = 1/2 |U|^2 [m^2/s^2]."""
    return 0.5 * (df["av_u_0"] ** 2 + df["av_u_1"] ** 2 + df["av_u_2"] ** 2)


# ----------------------------------------------------------------------
# Per-layer statistics
# ----------------------------------------------------------------------
def per_layer_stats(layers: dict[int, pd.DataFrame]) -> pd.DataFrame:
    rows = []
    for n, df in layers.items():
        k = tke(df).mean()
        ke = mean_flow_ke(df).mean()
        rows.append({"layer": n, "k": k, "k_mean": ke, "ratio": k / ke})
    return pd.DataFrame(rows).sort_values("layer").reset_index(drop=True)


def cov(x) -> float:
    """Coefficient of variation (%)."""
    x = np.asarray(x, float)
    return 100.0 * x.std(ddof=0) / x.mean()


# ----------------------------------------------------------------------
# Figures
# ----------------------------------------------------------------------
COLORS = {100: "#1f77b4", 300: "#d62728"}


def plot_perlayer(stats: dict[int, pd.DataFrame], outfile: Path) -> None:
    fig, ax = plt.subplots(figsize=(6.2, 4.4))
    for Re, st in stats.items():
        ax.plot(
            st["layer"], st["ratio"],
            marker="o", ms=7, lw=2, color=COLORS[Re],
            label=(f"$Re_P = {Re}$  "
                   f"(CoV$_k$ = {cov(st['k']):.1f}%)"),
        )
    ax.set_xlabel("layer $n$", fontsize=14)
    ax.set_ylabel(r"$k / k_{\mathrm{mean}}$", fontsize=14)
    ax.set_title(f"Per-layer fluctuation energy ({TOPO}$^\\circ$, {POS})", fontsize=13)
    ax.tick_params(labelsize=12)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11, framealpha=0.9)
    all_layers = sorted({n for st in stats.values() for n in st["layer"]})
    ax.set_xticks(all_layers)
    fig.tight_layout()
    fig.savefig(outfile, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  wrote {outfile}")


def plot_field(layers_by_Re: dict[int, dict[int, pd.DataFrame]],
               field_layer: int, outfile: Path) -> None:
    # Stacked vertically; colorbars alternate left (top) / right (bottom).
    # Each row reserves an identical colorbar-width slot on BOTH sides (one real,
    # one invisible spacer) so the data boxes stay horizontally aligned.
    fig, axes = plt.subplots(2, 1, figsize=(9, 6.6))
    locations = ["left", "right"]
    for ax, Re, loc in zip(axes, sorted(layers_by_Re), locations):
        layers = layers_by_Re[Re]
        n = field_layer if field_layer in layers else sorted(layers)[len(layers) // 2]
        df = layers[n]
        x = df["Points_0"] * 1e3                       # mm
        z = (df["Points_2"] - df["Points_2"].min()) * 1e3   # layer-local mm
        k = tke(df)
        tcf = ax.tricontourf(x, z, k, levels=60, cmap="viridis")
        # tight, correctly-proportioned band that fills the axes box
        ax.set_box_aspect((z.max() - z.min()) / (x.max() - x.min()))

        other = "right" if loc == "left" else "left"
        div = make_axes_locatable(ax)
        cax = div.append_axes(loc, size="3.5%", pad=0.12)          # real colorbar
        spacer = div.append_axes(other, size="3.5%", pad=0.12)     # invisible, identical slot
        spacer.set_axis_off()
        cb = fig.colorbar(tcf, cax=cax)
        cax.yaxis.set_ticks_position(loc)
        cax.yaxis.set_label_position(loc)
        cb.set_label(r"$k$  [m$^2$/s$^2$]", fontsize=16)
        cb.ax.tick_params(labelsize=14)

        # y-axis on the side opposite its colorbar
        ax.yaxis.set_label_position(other)
        ax.yaxis.set_ticks_position(other)
        ax.set_xlabel(r"$\xi$  [mm]", fontsize=18)
        ax.set_ylabel(r"$z'$  [mm]", fontsize=18)
        ax.set_title(f"$Re_P = {Re}$  (L{n:02d})", fontsize=18)
        ax.tick_params(labelsize=15)
    fig.savefig(outfile, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  wrote {outfile}")


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    layers_by_Re = {Re: load_layers(d) for Re, d in RUN_DIRS.items()}

    print(f"\nTKE analysis  (topology {TOPO}deg, {POS})")
    stats = {}
    for Re, layers in layers_by_Re.items():
        st = per_layer_stats(layers)
        stats[Re] = st
        print(f"\nRe_P = {Re}   layers {list(st['layer'])}")
        print(st.to_string(index=False,
                           float_format=lambda v: f"{v:.4f}"))
        print(f"  layer-averaged k       = {st['k'].mean():.4f} m^2/s^2")
        print(f"  layer-averaged k/k_mean = {st['ratio'].mean():.3f}")
        print(f"  CoV(k) across layers    = {cov(st['k']):.1f}%")
        print(f"  CoV(k/k_mean)           = {cov(st['ratio']):.1f}%")

    plot_perlayer(stats, OUTDIR / f"fig_tke_perlayer_{TOPO}.png")
    plot_field(layers_by_Re, FIELD_LAYER, OUTDIR / f"fig_tke_field_{TOPO}.png")


if __name__ == "__main__":
    main()
