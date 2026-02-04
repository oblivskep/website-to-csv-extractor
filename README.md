Website → CSV Data Extractor (Python)

Turn any website listing into a clean CSV/Excel file.

This small Python tool extracts structured data (titles, prices, links, etc.) from a webpage using a simple config file.
Change the config → run the script → get output.csv.

What this is for

Product lists

Directories

Catalogs

Search results

Any repeating items on a page

You provide a URL and the fields you want. The script does the rest.

Example demo site
Books to Scrape
4

Demo URL:

https://books.toscrape.com/

Project structure
scraper/
 ├─ scraper.py
 ├─ config.yaml
 ├─ requirements.txt
 └─ output.csv

Installation
pip install -r requirements.txt

How it works

All customization happens in config.yaml.

Example:

url: "https://books.toscrape.com/"

items_selector: "article.product_pod"

fields:
  title: "h3 a::attr(title)"
  price: ".price_color"
  link: "h3 a::attr(href)"

Run
python scraper.py


Result:

output.csv


Ready to open in Excel / Google Sheets.

How to adapt to any website

Open the target website

Inspect the repeating item (right click → Inspect)

Find the CSS selector for the container

Find selectors for each field you want

Put them in config.yaml

Run the script

Example output
title	price	link
A Light in the Attic	£51.77	catalogue/a-light-in-the-attic_1000/index.html
What a client sends me

Website URL

Fields they want (title, price, link, etc.)

What they receive

Clean CSV / Excel file with the data

Requirements
requests
beautifulsoup4
pyyaml

Notes

Works for static websites (no login, no heavy JavaScript)

Fast, simple, reusable template for data extraction tasks
