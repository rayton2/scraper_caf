class SeleniumScraper:
    def __init__(self, url):
        self.url = url
        self.driver = None

    def init_driver(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def fetch_data(self):
        self.driver.get(self.url)
        # Implement the logic to scrape the table data here
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )
        # Example: Locate the table and extract data
        table_data = []
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
        table = self.driver.find_element("xpath", "//table")  # Adjust the XPath as needed
        rows = table.find_elements("tag name", "tr")
        
        for row in rows:
            cols = row.find_elements("tag name", "td")
            cols = [col.text for col in cols]
            table_data.append(cols)
        
        return table_data

    def close_driver(self):
        if self.driver:
            self.driver.quit()