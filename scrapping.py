import requests
from bs4 import BeautifulSoup
import csv

url = "https://timesofindia.indiatimes.com/home/headlines" # Define the URL of Times of India

# Set up headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

# Send request
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    print("Successfully fetched the page!")
else:
    print("Failed to fetch the page. Status Code:", response.status_code)
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract headlines
articles = soup.find_all("span", class_="w_tle")  # Class for headlines

# Prepare list to store data
news_data = []

# Extract headlines and URLs
for article in articles:
    headline = article.text.strip()
    link = "https://timesofindia.indiatimes.com" + article.a["href"]
    news_data.append([headline, link])

# Save data to CSV
csv_filename = "times_of_india_news.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline", "URL"])
    writer.writerows(news_data)
print(f"✅ Scraped {len(news_data)} news headlines and saved to {csv_filename}")

