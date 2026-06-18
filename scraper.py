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
    rating = book.find("p", class_="star-rating").text
    instock = book.find("p", class_="instock availability").text
    print(title, price, instock)