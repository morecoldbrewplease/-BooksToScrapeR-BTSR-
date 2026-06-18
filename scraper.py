import requests
from bs4 import BeautifulSoup
URL = "https://books.toscrape.com/"
response = requests.get(URL)
print(response.status_code)

nice = BeautifulSoup(response.text, "html.parser")
books = nice.find_all("article", class_="product_pod")
print(f"Found {len(books)} books")
#first = books[0]

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.find("p", class_="star-rating")["class"][1]
    instock = book.find("p", class_="instock availability").text.strip()
    print(title, price, instock)

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
print(parse_books(response.text) )