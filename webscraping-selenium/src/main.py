# File: /webscraping-selenium/webscraping-selenium/src/main.py
# pyright: ignore[reportMissingImports]

from scraper.selenium_scraper import SeleniumScraper
from utils.excel_writer import write_to_excel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def main():
    url = 'https://caf.mda.gov.br/consulta-publica/ufpa'
    # Inicializa o scraper
    scraper = SeleniumScraper(url)
    scraper.init_driver()
    
    try:
        # Extrai os dados da tabela
        data = scraper.fetch_data()
        
        # Escreve os dados em um arquivo Excel
        write_to_excel(data, 'dados_tabela_caf.xlsx')
    except Exception as e:
        print(f"[ERRO] Falha ao extrair ou salvar dados: {e}")
    finally:
        # Fecha o driver do Selenium
        print("Encerrado")
#        scraper.close_driver()

if __name__ == "__main__":
    main()