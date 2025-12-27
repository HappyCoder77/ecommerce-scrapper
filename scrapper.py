import time
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

    def fetch_html(self, url: str, retries: int = 3, delay: int = 2) -> str:
        """
        Fetch the HTML content with a retry strategy to handle network blips.

        Args:
            url: The URL to fetch.
            retries: Number of times to retry if it fails.
            delay: Seconds to wait between retries.
        """
        for i in range(retries):

            try:
                response = requests.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.text
            except requests.RequestException as e:

                if i < retries - 1:
                    print(
                        f"f [Warning] atempt {i + 1} failed for {url} retrying in {delay}s..."
                    )
                    time.sleep(delay)
                else:
                    print(f" [Error] All {retries} attempts failed for {url}.")
                    raise e

        return ""

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

    def scrape_all_pages(self) -> List[Product]:
        """Iterates through all pages using the 'Next' button."""

        all_products: List[Product] = []
        current_url: str | None = self.base_url

        while current_url:
            print(f"Scrapping: {current_url}")
            html = self.fetch_html(current_url)

            page_products = self.parse_products(html)
            all_products.extend(page_products)

            soup = BeautifulSoup(html, "html.parser")
            next_button = soup.find("li", class_="next")

            if next_button and next_button.a:
                relative_next = str(next_button.a.get("href"))

                if "catalogue/" in current_url:
                    current_url = (
                        f"https://books.toscrape.com/catalogue/{relative_next}"
                    )
                else:
                    current_url = f"https://books.toscrape.com/{relative_next}"

            else:
                current_url = None

        return all_products
