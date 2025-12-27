import requests
from bs4 import BeautifulSoup, Tag
from typing import List, Dict
from models import Product


class BookScrapper:
    """Class to handle scraping logic for books.toscrape.com."""

    def __init__(self) -> None:
        self.base_url = "https://books.toscrape.com/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

        self.RATING_MAP: Dict[str, float] = {
            "One": 1.0,
            "Two": 2.0,
            "Three": 3.0,
            "Four": 4.0,
            "Five": 5.0,
        }

    def fetch_html(self) -> str:
        """Fetch the HTML content from the URL."""

        response = requests.get(self.base_url, headers=self.headers)
        response.raise_for_status()

        return response.text

    def parse_products(self, html: str) -> List[Product]:
        """Extract book data and convert it into Product objects."""

        soup = BeautifulSoup(html, "html.parser")
        products: List[Product] = []
        book_elements = soup.find_all("article", class_="product_pod")

        for book in book_elements:
            h3_tag = book.h3

            if h3_tag is None or h3_tag.a is None:
                continue

            title = str(h3_tag.a.get("title", "Unknown Title"))
            price_tag = book.find("p", class_="price_color")

            if price_tag is None:
                continue

            price_text = price_tag.text
            clean_price_str = price_text.strip()[1:]

            relative_url = h3_tag.a.get("href", "")
            full_url = f"{self.base_url}{relative_url}"

            rating_tag = book.find("p", class_="star-rating")
            rating_value = 0.0

            if rating_tag:
                classes = rating_tag.get("class")

                if isinstance(classes, list):

                    for c in classes:

                        if c in self.RATING_MAP:
                            rating_value = self.RATING_MAP[c]

            try:
                clean_price = float(clean_price_str)
            except ValueError:
                import re

                match = re.search(r"(\d+\.\d+)", price_text)
                clean_price = float(match.group(1)) if match else 0.0
            new_product = Product(
                name=title, price=clean_price, url=full_url, rating=rating_value
            )
            products.append(new_product)

        return products
