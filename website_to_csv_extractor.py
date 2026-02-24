import requests
from bs4 import BeautifulSoup
import csv
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

url = config["url"]
items_selector = config["items_selector"]
fields = config["fields"]

response = requests.get(url, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

items = soup.select(items_selector)

rows = []

for item in items:
    row = {}
    for field_name, selector in fields.items():
        if "::attr(" in selector:
            sel, attr = selector.split("::attr(")
            attr = attr.replace(")", "")
            element = item.select_one(sel)
            row[field_name] = element.get(attr) if element else ""
        else:
            element = item.select_one(selector)
            row[field_name] = element.get_text(strip=True) if element else ""
    rows.append(row)

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields.keys())
    writer.writeheader()
    writer.writerows(rows)

print("Done. Data saved to output.csv")
