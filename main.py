from scrapper import BookScrapper


def run_app():
    scrapper = BookScrapper()
    print("--- Fetching data from Books to Scrape ---")

    try:
        html = scrapper.fetch_html()
        books = scrapper.parse_products(html=html)

        print(f"Found: {len(books)} books:\n")

        for book in books:
            print(f"-{book.name}: {book.price}")

    except Exception as e:
        print(f"An error ocurred: {e}")


if __name__ == "__main__":
    run_app()
