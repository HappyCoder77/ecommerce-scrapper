import csv
from typing import List
from models import Product


def export_to_csv(products: List[Product], filename: str = "books.csv") -> None:
    """
    Exports a list of Product objects to a CSV file.

    Args:
        products: A list of Product instances.
        filename: The name of the output file.
    """

    fieldnames = ["name", "price", "rating", "url"]

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for product in products:
                writer.writerow(
                    {
                        "name": product.name,
                        "price": product.price,
                        "rating": product.rating,
                        "url": product.url,
                    }
                )

        print(f"Successfully exported {len(products)} to {filename}")

    except IOError as e:
        print(f"Error writing csv file: {e}")
