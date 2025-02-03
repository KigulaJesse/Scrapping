import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.monitor.co.ug/uganda/news"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to fetch the page")

soup = BeautifulSoup(html_content, "html.parser")
articles = soup.find_all("li", class_=["col-1-1 ","medium-col-1-2","large-col-1-4"])

data = []
for article in articles:
    title = article.find("h3").text.strip() if article.find("h3") else "No Title"
    link = article.find("a")["href"] if article.find("a") else "No Link"
    data.append({"title": title, "link": link})

    if link.startswith("/"):
        link = URL + link

    data.append((title, link))

print(data[:5])  

csv_filename = "monitor_articles.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Link"])
    writer.writerows(data)

print(f"Data saved to {csv_filename}")