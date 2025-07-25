# File: /webscraping-selenium/webscraping-selenium/src/main.py

from scraper.selenium_scraper import SeleniumScraper
from utils.excel_writer import write_to_excel

def main():
    # Inicializa o scraper
    scraper = SeleniumScraper()
    scraper.init_driver()
    
    try:
        # Extrai os dados da tabela
        data = scraper.fetch_data()
        
        # Escreve os dados em um arquivo Excel
        write_to_excel(data, 'dados_tabela.xlsx')
    finally:
        # Fecha o driver do Selenium
        scraper.close_driver()

if __name__ == "__main__":
    main()