from scrapper import BookScrapper
from exporter import export_to_csv


def run_app():
    scrapper = BookScrapper()
    print("--- Fetching data from Books to Scrape ---")

    try:
        books = scrapper.scrape_all_pages()

        print(f"Found: {len(books)} books:\n")

        if books:
            export_to_csv(books)
            print("Process finished successfully!")
        else:
            print("No data found to export.")

    except Exception as e:
        print(f"An error ocurred: {e}")


if __name__ == "__main__":
    run_app()
