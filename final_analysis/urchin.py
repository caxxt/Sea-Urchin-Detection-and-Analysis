import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

rows = []
for f in Path('/Users/cat/Downloads/campbell_river_dec_labels/').glob("*.txt"):
    with open(f) as file:
        count = sum(1 for _ in file)

    rows.append({
        "image": f.stem,
        "count": count
    })

df = pd.DataFrame(rows)

df[["month", "day", "hour"]] = df["image"].str.extract(r"_([a-zA-Z]+)(\d+)_(\d+)$")
df["time"] = df["hour"].map({"0": "night", "12": "noon"})

print(df)

# december plot internal
dec_df = df[df["month"] == "dec"]

avg_noon = dec_df[dec_df["time"] == "noon"]["count"].mean()
avg_night = dec_df[dec_df["time"] == "night"]["count"].mean()

pivot_dec = dec_df.pivot(index="day", columns="time", values="count").sort_index()

pivot_dec.plot(kind="bar", figsize=(12,6))

plt.axhline(avg_noon, linestyle="--", color="red", label="Noon Average")
plt.axhline(avg_night, linestyle="--", color="blue", label="Night Average")

plt.xlabel("Day of Month")
plt.ylabel("Urchin Count")
plt.title("December Urchin Counts: Noon vs Night")
plt.xticks(rotation=0)

plt.legend()
plt.tight_layout()
plt.show()

# august plot internal
aug_df = df[df["month"] == "aug"]

avg_noon = aug_df[aug_df["time"] == "noon"]["count"].mean()
avg_night = aug_df[aug_df["time"] == "night"]["count"].mean()

pivot_aug = aug_df.pivot(index="day", columns="time", values="count").sort_index()

pivot_aug.plot(kind="bar", figsize=(12,6))

plt.axhline(avg_noon, linestyle="--", color="red", label="Noon Average")
plt.axhline(avg_night, linestyle="--", color="blue", label="Night Average")

plt.xlabel("Day of Month")
plt.ylabel("Urchin Count")
plt.title("August Urchin Counts: Noon vs Night")
plt.xticks(rotation=0)

plt.legend()
plt.tight_layout()
# plt.savefig("aug_urchin_daysvsnight.png")
plt.show()

# dec vs aug total pop
month_avg = df.groupby("month")["count"].mean()

month_avg.loc[["aug","dec"]].plot(kind="bar", color=["orange","blue"])

plt.ylabel("Average Urchin Count")
plt.title("Average Urchin Population: August vs December")
plt.xticks(rotation=0)

plt.tight_layout()
# plt.savefig("decvsaug_total_pop.png")
plt.show()

# dec vs aug noon and night pop
pivot_month = df.groupby(["month","time"])["count"].mean().unstack()

pivot_month.loc[["aug","dec"]].plot(kind="bar", figsize=(8,5))

plt.ylabel("Average Urchin Count")
plt.title("Average Urchin Population by Month and Time")
plt.xticks(rotation=0)

plt.tight_layout()
# plt.savefig("decvsaug_time.png")
plt.show()