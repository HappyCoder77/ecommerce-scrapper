# Books to Scrape: Professional ETL Pipeline

A robust, type-safe web scraper built with Python that extracts 1,000 book records from a live demo site. This project follows clean architecture principles and a feature-based Git workflow.

## 🚀 Features

- **Full Catalog Scraping:** Automatically navigates through 50 pages of content to collect 1,000 products.
- **Resilient ETL Pipeline:** \* **Extract:** Efficient HTML fetching with a custom retry strategy and timeouts.
  - **Transform:** Data cleaning, price normalization, and rating mapping (text-to-numeric).
  - **Load:** Clean export to structured CSV format.
- **Type Safety:** 100% static type checking coverage with `mypy`.
- **Enhanced UX:** Real-time visual progress monitoring via `tqdm`.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** Requests, BeautifulSoup4, tqdm
- **Dev Tools:** Mypy (Type Checking), Flake8 (Linting)
- **Workflow:** Git Flow with atomic, feature-based commits.

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/HappyCoder77/ecommerce-scrapper.git
   cd ecommerce-scrapper

   ```

2. **Set up virtual environment:**

   ```bash
   python3 -m venv ecommerce-scrapper-env
   source ecommerce-scrapper-env/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## 🖥️ Usage

Run the main script to start the extraction process:

```bash
python3 main.py
```

## 🛡️ Quality Assurance

Run type checking to ensure code integrity:

```bash
mypy ./scrapper.py
```
