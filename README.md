# Fintech Review Analytics

## Objective

Analyze Google Play Store reviews for Ethiopian banks to extract sentiment and themes.

## Data Collection

- Source: Google Play Store
- Tools: google-play-scraper
- Banks:
  - Commercial Bank of Ethiopia (CBE)
  - Bank of Abyssinia (BOA)
  - Dashen Bank
- Reviews collected: 400+ per bank (target 1200 total)

## Methodology

- Scraped review text, rating, date, bank name
- Used newest-first sorting
- Limited by Google Play API rate limits

## Preprocessing

- Removed duplicates
- Dropped missing values
- Normalized dates to YYYY-MM-DD
- Selected required columns only:
  review, rating, date, bank, source

## Limitations

- Some banks may have fewer reviews due to API constraints
- Future improvement: pagination + longer time range scraping
