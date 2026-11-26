"""Generate both Chinese background figures from the four original PubMed exports."""
import csv
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
YEARS = range(2021, 2026)
plt.rcParams.update({"font.family": ["Noto Sans CJK JP", "DejaVu Sans"], "pdf.fonttype": 42})
BLUE, TEAL = "#345886", "#097669"


def counts(suffix):
    path = ROOT / "pubmed" / f"PubMed_Timeline_Results_by_Year{suffix}.csv"
    with path.open(encoding="utf-8-sig", newline="") as source:
        next(source)  # PubMed writes the search expression before the CSV header.
        records = {int(r["Year"]): int(r["Count"]) for r in csv.DictReader(source)}
    return [records.get(year, 0) for year in YEARS]


import matplotlib.ticker as mtick
import numpy as np

years = list(YEARS)
causal_broad_yr = counts(" (1)")
causal_narrow_yr = counts(" (2)")
corr_broad_5yr = sum(counts(" (3)"))
corr_narrow_5yr = sum(counts(""))
causal_broad_5yr = sum(causal_broad_yr)
causal_narrow_5yr = sum(causal_narrow_yr)
# Ratios and YoY calculations
narrow_ratio = causal_narrow_5yr / corr_narrow_5yr * 100
broad_ratio = causal_broad_5yr / corr_broad_5yr * 100

# Create figure with 2 subplots (side-by-side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.8, 3.65), dpi=300)
fig.patch.set_facecolor('white')

# --- Left Panel: 5-Year Totals Comparison (2021-2025) ---
categories = ['宽泛检索（体育）', '精确检索（运动损伤）']
x = np.arange(len(categories))
width = 0.34

corr_vals = [corr_broad_5yr, corr_narrow_5yr]
causal_vals = [causal_broad_5yr, causal_narrow_5yr]

rects1 = ax1.bar(x - width/2, corr_vals, width, label='相关性词', color='#3B6998', edgecolor='none', zorder=3)
rects2 = ax1.bar(x + width/2, causal_vals, width, label='因果推断词', color='#D95F02', edgecolor='none', zorder=3)

ax1.set_yscale('log')
ax1.set_ylim(1, 42000)
ax1.set_ylabel('五年命中数（篇次，对数刻度）', fontsize=10.5, fontweight='bold', color='#222222')
ax1.set_title('2021–2025 年两组检索词的五年总量', fontsize=11.5, fontweight='bold', pad=12, color='#111111')
ax1.set_xticks(x)
ax1.set_xticklabels(categories, fontsize=10, fontweight='bold', color='#222222')
ax1.grid(axis='y', linestyle='--', alpha=0.45, zorder=0)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

for rect in rects1:
    h = rect.get_height()
    ax1.annotate(f'{int(h):,}',
                 xy=(rect.get_x() + rect.get_width()/2, h),
                 xytext=(0, 4), textcoords="offset points",
                 ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#2B4C7E')

for rect in rects2:
    h = rect.get_height()
    ax1.annotate(f'{int(h):,}',
                 xy=(rect.get_x() + rect.get_width()/2, h),
                 xytext=(0, 4), textcoords="offset points",
                 ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#B24700')

# Add ratio callout annotations
ax1.text(0, 24000, f'因果词／相关词 {broad_ratio:.2f}%', ha='center', va='center',
         fontsize=8.8, bbox=dict(boxstyle='round,pad=0.3', facecolor='#F2F5F9', edgecolor='#B8C7D9'))
ax1.text(1, 1600, f'因果词／相关词 {narrow_ratio:.2f}%', ha='center', va='center',
         fontsize=8.8, bbox=dict(boxstyle='round,pad=0.3', facecolor='#FDF3EC', edgecolor='#E8C3A9'))

ax1.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='#DDDDDD', fontsize=9.5)

# --- Right Panel: Annual Trend of Causal Inference (2021-2025) ---
x_yr = np.arange(len(years))
line1 = ax2.plot(x_yr, causal_broad_yr, marker='o', linewidth=2.4, markersize=7.5,
                 color='#D95F02', label='宽泛检索（合计 129）', zorder=4)
line2 = ax2.plot(x_yr, causal_narrow_yr, marker='s', linewidth=2.2, markersize=6.8,
                 linestyle='--', color='#1B9E77', label='精确检索（合计 7）', zorder=4)

ax2.fill_between(x_yr, causal_broad_yr, color='#D95F02', alpha=0.10, zorder=2)

ax2.set_ylim(-1.5, 48)
ax2.set_ylabel('年度命中数（篇次）', fontsize=10.5, fontweight='bold', color='#222222')
ax2.set_title('因果推断词的年度命中数与同比变化', fontsize=11.5, fontweight='bold', pad=12, color='#111111')
ax2.set_xticks(x_yr)
ax2.set_xticklabels(years, fontsize=10, fontweight='bold', color='#222222')
ax2.yaxis.set_major_locator(mtick.MultipleLocator(5))
ax2.grid(axis='y', linestyle='--', alpha=0.45, zorder=0)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

for i, val in enumerate(causal_broad_yr):
    yoy_str = ""
    if i > 0 and causal_broad_yr[i-1] > 0:
        pct = (val - causal_broad_yr[i-1]) / causal_broad_yr[i-1] * 100
        yoy_str = f"\n({pct:+.0f}%)" if pct != 0 else "\n(0%)"
    ax2.annotate(f'{val}{yoy_str}',
                 xy=(x_yr[i], val),
                 xytext=(0, 7), textcoords="offset points",
                 ha='center', va='bottom', fontsize=8.8, fontweight='bold', color='#B24700')

for i, val in enumerate(causal_narrow_yr):
    offset_y = 6
    ax2.annotate(f'{val}',
                 xy=(x_yr[i], val),
                 xytext=(0, offset_y), textcoords="offset points",
                 ha='center', va='top' if offset_y < 0 else 'bottom',
                 fontsize=8.8, fontweight='bold', color='#136F53')

ax2.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='#DDDDDD', fontsize=9)

plt.tight_layout(pad=.6, w_pad=2.2)
plt.savefig(ROOT / 'figures/pubmed-comparison-cn.pdf', bbox_inches='tight', pad_inches=.04)
print("Saved chart successfully.")