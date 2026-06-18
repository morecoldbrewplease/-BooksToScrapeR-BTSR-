from pathlib import Path

import matplotlib

matplotlib.use("Agg") 
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/books.csv")
Path("charts").mkdir(exist_ok=True)

counts = df["rating"].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(counts.index, counts.values, color="#4c72b0")
ax.set_title("Books per rating")
ax.set_xlabel("Rating (stars)")
ax.set_ylabel("Number of books")
fig.savefig("charts/books_per_rating.png", bbox_inches="tight")
plt.close(fig)

fig, ax = plt.subplots()
ax.hist(df["price"], bins=20, color="#55a868", edgecolor="white")
ax.set_title("Distribution of prices")
ax.set_xlabel("Price (£)")
ax.set_ylabel("Number of books")
fig.savefig("charts/price_distribution.png", bbox_inches="tight")
plt.close(fig)

avg_price = df.groupby("rating")["price"].mean()
fig, ax = plt.subplots()
ax.bar(avg_price.index, avg_price.values, color="#c44e52")
ax.set_title("Average price per rating")
ax.set_xlabel("Rating (stars)")
ax.set_ylabel("Average price (£)")
fig.savefig("charts/avg_price_per_rating.png", bbox_inches="tight")
plt.close(fig)

print("Saved 3 charts to charts/")
for p in sorted(Path("charts").glob("*.png")):
    print(f"  {p}")
