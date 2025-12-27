from models import Product


def run_test():
    # Creating a sample product instance
    # Note: price is a float and rating is Optional
    sample_item = Product(
        name="Python Crash Course",
        price=25.99,
        rating=4.8,
        url="https://example.com/python-book",
    )

    print("-----------Product test-----------")
    print(f"Product name: {sample_item.name}")
    print(f"Formated price: {sample_item.price:.2f}")
    print(f"Full object: {sample_item}")


if __name__ == "__main__":
    run_test()
