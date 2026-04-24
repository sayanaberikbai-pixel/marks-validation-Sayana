import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


df = pd.read_csv("marks.csv")
df["points_num"] = pd.to_numeric(df["points"], errors="coerce")
df["ok"] = df["points_num"].notna() & df["points_num"].between(0, 100)

valid_count = int(df["ok"].sum())
invalid_count = int((~df["ok"]).sum())


fig, ax = plt.subplots(figsize=(7, 5))
fig.patch.set_facecolor("#0d1117")
ax.set_facecolor("#161b22")

bars = ax.bar(
    ["Жарамды\n(Valid)", "Жарамсыз\n(Invalid)"],
    [valid_count, invalid_count],
    color=["#2ea043", "#da3633"],
    edgecolor="#30363d",
    linewidth=1.5,
    width=0.5,
)


for bar, val in zip(bars, [valid_count, invalid_count]):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.3,
        str(val),
        ha="center", va="bottom",
        color="white", fontsize=16, fontweight="bold",
    )

ax.set_title("marks.csv — Баллдарды тексеру нәтижесі", color="white", fontsize=14, pad=14)
ax.set_ylabel("Жолдар саны", color="#8b949e", fontsize=11)
ax.tick_params(colors="white", labelsize=12)
ax.spines[["top", "right", "left", "bottom"]].set_color("#30363d")
ax.yaxis.label.set_color("#8b949e")
ax.set_ylim(0, max(valid_count, invalid_count) + 3)
ax.yaxis.set_tick_params(labelcolor="#8b949e")

plt.tight_layout()
plt.savefig("validation_bar.png", dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close()


print("— Bar диаграмма")

print(f" Жарамды  : {valid_count}")
print(f" Жарамсыз : {invalid_count}")
print("validation_bar.png сақталды!")
