# Web Scraping with Selenium

This project is a Python application that uses Selenium to scrape tables from the Brazilian public data website CAF (Cadastro Nacional de Agricultura Familiar - National Registry for Family Agriculture), and records the extracted data into an Excel file. The main goal is to cross-reference this data with private company databases about their potential clients, identifying weather they are properly registered, improving their outreach to the public. 

## Project Structure

This project is built in the following structure:

```
webscraping-selenium
├── src
│   ├── main.py                # Starting point
│   ├── scraper
│   │   └── selenium_scraper.py # Class responsible for the scraping
│   └── utils
│       └── excel_writer.py     # Function responsible for recording the data in Excel
├── requirements.txt            # Dependencies
└── README.md                   # Documentation
```

## Prerequisites

Before running the project, make sure you have Python installed on your machine. You will also need ChromeDriver or another driver compatible with the browser you intend to use.

## Installation

1. Clone the repository:
   ```
   git clone <Repository_URL>
   cd webscraping-selenium
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Configure the Selenium driver in the `src/scraper/selenium_scraper.py` file as needed.
2. Run the scraper:
   ```
   python src/main.py
   ```

The extracted data will be saved into an Excel file as defined in the `write_to_excel` function in the file `src/utils/excel_writer.py`.

## Contribution

Feel free to contributr with improving and corrections. 
Sinta-se à vontade para contribuir com melhorias ou correções. Fork the repository and submit a pull request with your changes.