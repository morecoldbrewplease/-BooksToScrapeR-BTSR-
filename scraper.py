import time
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"


def parse_books(html):
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
    all_books = []
    page = 1
    while True:
        url = BASE_URL.format(page)
        response = requests.get(url)
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
