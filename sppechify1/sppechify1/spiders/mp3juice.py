import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MP3Spider(scrapy.Spider):
    name = 'mp3juice'
    start_urls = ['https://v3.mp3juices.click/']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def parse(self, response):
        self.driver.get(response.url)

        # Simulate a search query
        search_box = self.driver.find_element(By.XPATH, "//input[@name='url']")
        search_box.send_keys("Justin Bieber - Hold On")  # Replace with your song name
        search_box.send_keys(Keys.RETURN)  # Submit search by pressing Enter

        self.driver.implicitly_wait(5)  # Wait for results to load

        # Extract download links
        links = self.driver.find_elements("xpath", "//a[contains(@class, 'download MP3')]")
        for link in links:
            yield {"mp3_url": link.get_attribute("href")}

        self.driver.quit()



