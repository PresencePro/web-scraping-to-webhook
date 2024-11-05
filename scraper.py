import requests
from bs4 import BeautifulSoup

# Replace with the URL of the page you want to scrape
source_url = "https://hdhub4u.capetown"  # Replace with the actual URL
webhook_url = "YOUR_WEBHOOK_URL"  # Replace with your actual Pabbly webhook URL

# Step 1: Fetch the web page
response = requests.get(source_url)
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all the movie containers by their class
    movies = soup.find_all("li", class_="thumb col-md-2 col-sm-4 col-xs-6")
    
    for movie in movies:
        # Extract image URL
        img_tag = movie.find("img")
        img_url = img_tag['src'] if img_tag else None

        # Extract movie title
        title = img_tag['alt'] if img_tag else None

        # Extract link
        link_tag = movie.find("a")
        link_url = link_tag['href'] if link_tag else None

        # Prepare data for webhook
        data = {
            "title": title,
            "image_url": img_url,
            "link": link_url
        }

        # Send data to Pabbly webhook
        response = requests.post(webhook_url, json=data)
        if response.status_code == 200:
            print("Data sent successfully to Pabbly for:", title)
        else:
            print("Failed to send data to Pabbly:", response.status_code)
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
