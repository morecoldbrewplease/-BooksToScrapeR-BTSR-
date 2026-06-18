import pandas as pd

df = pd.read_csv("data/books.csv")

print(f"Total books: {len(df)}")
print(f"Average price overall: £{df['price'].mean():.2f}")

print("\nAverage price per rating:")
print(df.groupby("rating")["price"].mean().round(2))

print("\nNumber of books per rating:")
print(df["rating"].value_counts().sort_index())

print("\n10 most expensive books:")
print(df.nlargest(10, "price")[["title", "price", "rating"]].to_string(index=False))

in_stock = (df["availability"] == "In stock").sum()
print(f"\nBooks in stock: {in_stock} of {len(df)}")
