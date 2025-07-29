# File: /webscraping-selenium/webscraping-selenium/src/main.py

from scraper.selenium_scraper import SeleniumScraper
from utils.excel_writer import write_to_excel

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
        scraper.close_driver()

if __name__ == "__main__":
    main()