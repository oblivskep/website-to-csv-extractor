# 🌐 Website → CSV Data Extractor (Python)

> Extract structured data from public websites and deliver it as clean CSV/Excel files.

This small Python tool uses a simple configuration file to collect repeating items (titles, prices, links, etc.) from a webpage and export them into `output.csv`.

Change the config → run the script → get a spreadsheet.

---

## 🧩 What this is for

- Product listings
- Directories
- Catalogs
- Search results
- Any page with repeating items

You provide a URL and the fields you want. The script does the rest.

---

## Visual Schema

```text
+---------------------------+
| Target Website URL        |
+---------------------------+
             |
             v
+---------------------------+
| Config File (config.yaml) |
| URL + selectors + fields  |
+---------------------------+
             |
             v
+---------------------------+
| scraper.py                |
| fetch + parse + extract   |
+---------------------------+
             |
             v
+---------------------------+
| Structured Output         |
| output.csv / Excel-ready  |
+---------------------------+
```

---

## ▶️ Example Demo Site

Demo used in this repository:

Books to Scrape  
https://books.toscrape.com/

### Source website example
![Website example](site_example.png)

### Output CSV example
![CSV example](example_output.png)

---

## 📁 Project structure

scraper.py  
config.yaml  
requirements.txt  
README.md  
site_example.png  
example_output.png  

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## 🛠 How it works

All customization happens in **config.yaml**.

Example used for the demo site:

```yaml
url: "https://books.toscrape.com/"

items_selector: "article.product_pod"

fields:
  title: "h3 a::attr(title)"
  price: ".price_color"
  link: "h3 a::attr(href)"
```

---

## ▶️ Run

```bash
python scraper.py
```

The result will be:

output.csv

Ready to open in Excel or Google Sheets.

---

## 🔎 How to adapt to any website

1. Open the target website
2. Right click an item → Inspect
3. Find the CSS selector for the repeating container
4. Find selectors for the fields you want
5. Put them into `config.yaml`
6. Run the script

---

## 📦 What a client sends

- Website URL
- Fields they want (title, price, link, etc.)

## 📤 What they receive

- Clean CSV / Excel file with the extracted data

---

## 📋 Requirements

requests  
beautifulsoup4  
pyyaml  

---

## ✅ Notes

- Designed for public, static websites (no login required)
- Fast, simple, reusable template for real data extraction tasks

---

## License

MIT License. See `LICENSE`.
