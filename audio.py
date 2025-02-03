import requests
from bs4 import BeautifulSoup

URL = "https://example-podcast.com"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    html_contenct = response.text
else:
    print("Failed to fetch the page")

soup = BeautifulSoup(response.text, "html.parser")

audio_links = soup.find_all("a", href=True)
audio_urls = [link['href'] for link in audio_links if link['href'].endswith('.mp3')]

print(audio_urls)


