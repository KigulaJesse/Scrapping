from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

# Initialize WebDriver with Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)  # Use the service to initialize

def search_for_song():
    # Open the target website
    driver.get("https://v3.mp3juices.click/")  # Replace with the actual URL

    # Find the search box
    search_box = driver.find_element(By.XPATH, "//input[@name='url']")
    search_box.send_keys("Justin Bieber - Hold On")  # Replace with your song name
    search_box.send_keys(Keys.RETURN)  # Submit search by pressing Enter

    # # Wait for the results to load (adjust XPath to match results' element)
    try:
        results = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@class, 'download MP3')]"))
        )

        print(results)

        if results:
            # Get the href of the first MP3 link
            mp3_url = results[0].get_attribute("href")
            print("MP3 URL found:", mp3_url)

            # Download the MP3 file using requests
            response = requests.get(mp3_url)
            
            # Save the file to disk
            with open("Justin_Bieber_Hold_On.mp3", "wb") as file:
                file.write(response.content)
            print("Download complete!")
        else:
            print("No results found.")
    except:
        print("Search timed out or no results found.")

# Run the function to perform the search
search_for_song()

# Close the driver when done
driver.quit()
