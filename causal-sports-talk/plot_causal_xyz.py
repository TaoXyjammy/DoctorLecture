"""Render the running-equipment illustration for the Chinese interview deck."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

plt.rcParams["font.family"] = ["DejaVu Sans", "Noto Sans CJK JP"]
fig, ax = plt.subplots(figsize=(4.4, 3.55))
ax.set(xlim=(0, 10), ylim=(0, 8.6))
ax.set_axis_off()
orange, gray, green = "#C25900", "#4B5563", "#0F766E"


def node(x, y, letter, caption, caption_y, face, edge, ink):
    ax.add_patch(FancyBboxPatch((x-.625, y-.41), 1.25, .82,
                 boxstyle="round,pad=.03,rounding_size=.10",
                 facecolor=face, edgecolor=edge, linewidth=1.3, zorder=3))
    ax.text(x, y, letter, ha="center", va="center", fontsize=12,
            weight="bold", color=ink)
    ax.text(x, caption_y, caption, ha="center", va="center", fontsize=9, color=ink)


def path(start, end, color, style, curvature, caption, label_pos, arrow=True):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>" if arrow else "-",
                 mutation_scale=10, connectionstyle=f"arc3,rad={curvature}",
                 linewidth=1.2, linestyle=style, color=color))
    ax.text(*label_pos, caption, ha="center", va="center", fontsize=8,
            color=color, bbox=dict(facecolor="white", edgecolor="none", pad=.7))


node(5, 6.75, "Z", "Z：既往伤病史 / 早期疼痛", 7.65, "#FFF7ED", orange, "#7C2D12")
node(2, 3.05, "X", "X：护具 / 缓震装备", 2.18, "#EFF6FF", "#2563EB", "#1E3A8A")
node(8, 3.05, "Y", "Y：后续运动损伤", 2.18, "#FEF2F2", "#DC2626", "#7F1D1D")
path((4.25, 6.42), (2.15, 3.60), orange, "-", .08, "影响装备选择", (2, 5.2))
path((5.75, 6.42), (7.85, 3.60), orange, "-", -.08, "增加损伤风险", (8, 5.2))
path((2.72, 3.22), (7.28, 3.22), gray, "--", 0, "观测统计关联", (5, 3.63), False)
path((7.28, 2.86), (2.72, 2.86), green, ":", -.18, "反向/适应性反馈", (5, 2.05))
legend = [Line2D([0], [0], color=c, linestyle=s, label=t)
          for c, s, t in [(orange, "-", "混杂路径（Z → X，Z → Y）"),
                          (gray, "--", "观测关联（X — Y）"),
                          (green, ":", "反向反馈（Y ···> X）")]]
ax.legend(handles=legend, loc="lower center", fontsize=7.3, labelspacing=.18,
          borderpad=.32, facecolor="#FAFAFA", edgecolor="#D1D5DB")
ax.add_patch(FancyBboxPatch((.15, .05), 9.7, 8.45, boxstyle="square,pad=0",
             facecolor="none", edgecolor="#D1D5DB", linewidth=.75))
fig.subplots_adjust(left=.02, right=.98, top=.98, bottom=.02)
fig.savefig(Path(__file__).parent / "figures/causal_xyz_nature_cn.png", dpi=300,
            bbox_inches="tight", pad_inches=.04)
