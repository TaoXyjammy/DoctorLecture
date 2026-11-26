"""Plot verified WoS annual publication counts for the Beamer deck."""
import csv
import sys

import matplotlib.pyplot as plt

with open(sys.argv[1], encoding="utf-8-sig", newline="") as source:
    rows = sorted(({k: int(r[k]) for k in ("year", "association", "causal", "both")}
                   for r in csv.DictReader(source)), key=lambda r: r["year"])
years = [r["year"] for r in rows]
if years != list(range(2021, 2026)):
    raise ValueError("Expected one verified row per year from 2021 to 2025")
if any(not 0 <= r["both"] <= min(r["association"], r["causal"]) for r in rows):
    raise ValueError("Invalid overlap or negative count")
fig, ax = plt.subplots(figsize=(8.2, 4), layout="constrained")
counts = [r["causal"] for r in rows]
ax.bar_label(ax.bar(years, counts, color="#145EAD"), padding=3)
ax.set(xticks=years, ylabel="Articles", ylim=(0, max(1, max(counts))*1.20),
       title="Causal-inference keyword matches in Sport Sciences")
fig.supxlabel("WoS Core Collection, 2021–2025   |   " + "   ".join(
    f"{label}: {sum(r[key] for r in rows):,}"
    for key, label in [("association", "Correlation"), ("causal", "Causal"), ("both", "Overlap")]), fontsize=10)
fig.savefig("wos-trend.pdf")
