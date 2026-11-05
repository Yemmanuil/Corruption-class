
import matplotlib.pyplot as plt

# 1. Enter the EuroPAM data
data = {
    "Serbia": 92,
    "Croatia": 88,
    "Bulgaria": 75,
    "Ukraine": 71,
    "European Union": 61,
    "Portugal": 59,
    "France": 57,
    "EU average": 52,
    "Poland": 47,
    "Italy": 46,
    "Denmark": 16,
    "Belgium": 11
}

# 2. Sort the data from highest to lowest
sorted_data = sorted(
    data.items(),
    key=lambda item: item[1],
    reverse=True
)

countries = [item[0] for item in sorted_data]
scores = [item[1] for item in sorted_data]

# 3. Assign different colours to EU indicators
colors = []

for country in countries:
    if country == "European Union":
        colors.append("#D97706")  # Orange
    elif country == "EU average":
        colors.append("#16A085")  # Green
    else:
        colors.append("#4472C4")  # Blue

# 4. Create the chart
fig, ax = plt.subplots(figsize=(11, 7))

bars = ax.barh(
    countries,
    scores,
    color=colors,
    height=0.65
)

# Highest score at the top
ax.invert_yaxis()

# 5. Display scores at the end of each bar
for bar, score in zip(bars, scores):
    ax.text(
        score + 1,
        bar.get_y() + bar.get_height() / 2,
        str(score),
        va="center",
        fontsize=11,
        fontweight="bold"
    )

# 6. Chart title and labels
ax.set_title(
    "Conflict of Interest: Comparison Across Countries",
    fontsize=16,
    fontweight="bold",
    pad=20
)

ax.set_xlabel("Conflict of Interest Score", fontsize=12)

# 7. Set the scale
ax.set_xlim(0, 105)
ax.set_xticks(range(0, 101, 10))

# 8. Improve chart appearance
ax.grid(
    axis="x",
    linestyle="--",
    alpha=0.3
)

ax.set_axisbelow(True)

# Remove unnecessary borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 9. Add legend
from matplotlib.patches import Patch

legend_items = [
    Patch(facecolor="#4472C4", label="Countries"),
    Patch(facecolor="#D97706", label="European Union"),
    Patch(facecolor="#16A085", label="EU average")
]

ax.legend(
    handles=legend_items,
    loc="lower right",
    frameon=False
)

# Add source note below the chart
fig.text(
    0.01,
    0.015,
    "Figure 1. Source: EuroPAM, 2024 data (may not include recent changes). "
    "Scores 0-100: higher = more complete formal rules.",
    fontsize=9,
    ha="left"
)

# Leave space for the source note
plt.tight_layout(rect=[0, 0.07, 1, 1])

    
