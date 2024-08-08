# Scrapy Project


## Overview

This project is all about scraping product details from the RS Components website. Specifically, we're focusing on the page for [Disposable Respirator 2012391](https://uk.rs-online.com/web/p/disposable-respirators/2012391). 

With this Scrapy spider, we pull out key information about the product, like stock numbers, manufacturer details, pricing, and more. Here's what we’re capturing:

- **Tags**: Any relevant tags .
- **RS Stock Number**: The unique stock number assigned by RS Components.
- **Manufacturer Part Number**: The part number given by the manufacturer.
- **Brand**: The brand of the product.
- **Price Excluding VAT**: The price before VAT, formatted with the PKR currency symbol.
- **Price Including VAT**: The price with VAT included, rounded to 3 decimal places and formatted with the PKR currency symbol.
- **Stock**: How much of the product is available.
- **Image**: The URL to the product image.

The `ProductItem` class is used to define what data we’re interested in and how it should be formatted.





## Project Structure

\```plaintext
scrapy_product/
├── __init__.py
├── items.py
├── middlewares.py
├── pipelines.py
├── settings.py
└── spiders/
    ├── __init__.py
    └── product_spider.py
├── scrapy.cfg
├── requirements.txt
└── README.md
\```

- **scrapy_product/**: The main project directory containing settings, items, and spiders.
- **scrapy_product/items.py**: Defines the items you want to scrape.
- **scrapy_product/spiders/**: Contains your spider files.
- **scrapy.cfg**: Scrapy project configuration file.
- **requirements.txt**: Lists project dependencies.


## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/scrapy_project.git
   cd scrapy_project


2. **Create a Virtual Environment**
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. **Install Dependencies**
    `pip install -r requirements.txt`

## Usage

### Run the Spider

scrapy crawl product_spider