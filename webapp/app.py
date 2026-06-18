from pathlib import Path

import pandas as pd
from flask import Flask, render_template

BASE_DIR = Path(__file__).resolve().parent.parent
CSV = BASE_DIR / "data" / "books.csv"

app = Flask(__name__)


def load_df():
    return pd.read_csv(CSV)


@app.route("/")
def index():
    df = load_df()
    stats = {
        "total": len(df),
        "avg_price": round(df["price"].mean(), 2),
        "avg_rating": round(df["rating"].mean(), 2),
        "in_stock": int((df["availability"] == "In stock").sum()),
    }
    charts = [
        ("Books per rating", "charts/books_per_rating.png"),
        ("Price distribution", "charts/price_distribution.png"),
        ("Average price per rating", "charts/avg_price_per_rating.png"),
    ]
    return render_template("index.html", stats=stats, charts=charts)


@app.route("/books")
def books():
    df = load_df()
    return render_template("books.html", books=df.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True)
