"""Scrape every book from books.toscrape.com and save a clean CSV.

Run directly (`python scraper.py`) to crawl all 50 pages, clean the data with
pandas, and write the result to data/books.csv.
"""

import time
from pathlib import Path

import requests
import pandas as pd
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def parse_books(html):
    """Parse one page of HTML into a list of book dicts (title, price, rating, availability)."""
    soup = BeautifulSoup(html, "html.parser")
    results = []
    for article in soup.find_all("article", class_="product_pod"):
        results.append({
            "title": article.h3.a["title"],
            "price": article.find("p", class_="price_color").text,
            "rating": article.find("p", class_="star-rating")["class"][1],
            "availability": article.find("p", class_="instock availability").text.strip(),
        })
    return results


def scrape_all():
    """Crawl every catalogue page until a 404, returning all books as a list of dicts."""
    all_books = []
    page = 1
    while True:
        url = BASE_URL.format(page)
        response = requests.get(url)
        response.encoding = "utf-8"  # site omits charset; force correct decoding of £
        if response.status_code == 404:
            break
        all_books += parse_books(response.text)
        print(f"Page {page}: {len(all_books)} books so far")
        page += 1
        time.sleep(1)
    return all_books


if __name__ == "__main__":
    books = scrape_all()
    print(f"\nDone. Scraped {len(books)} books total.")

    df = pd.DataFrame(books)
    df["price"] = df["price"].str.replace("£", "", regex=False).astype(float)
    df["rating"] = df["rating"].map(RATING_MAP)
    Path("data").mkdir(exist_ok=True)
    df.to_csv("data/books.csv", index=False)

    print(f"\nSaved {len(df)} rows to data/books.csv")
    print(df.head())
    print(df.dtypes)
