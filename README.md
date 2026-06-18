# BooksToScrapeR

A web-scraping learning project against [books.toscrape.com](https://books.toscrape.com):
scrape every book, clean the data with pandas, analyze it, and (later) visualize
and serve it. See [GUIDE.md](GUIDE.md) for the full phase-by-phase roadmap.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```powershell
python scraper.py    # scrape all 1000 books -> data/books.csv
python analyze.py    # print analysis of the scraped data
```

## Findings (Phase 6)

Analysis of all **1000 books** scraped from the site:

- **Average price:** £35.07
- **In stock:** 1000 of 1000 books
- **Average price per rating** is nearly flat — rating barely affects price:

  | Rating | Avg price | Count |
  |:------:|:---------:|:-----:|
  | ★1 | £34.56 | 226 |
  | ★2 | £34.81 | 196 |
  | ★3 | £34.69 | 203 |
  | ★4 | £36.09 | 179 |
  | ★5 | £35.37 | 196 |

- **Most expensive books** all cluster just under £60 (the site's apparent price
  ceiling). Top 3:
  1. The Perfect Play (Play by Play #1) — £59.99
  2. Last One Home (New Beginnings #1) — £59.98
  3. Civilization and Its Discontents — £59.95
