import requests
from bs4 import BeautifulSoup

# Replace with the URL of the page you want to scrape
source_url = "https://example.com/page-to-scrape"
webhook_url = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZjMDYzMjA0M2Q1MjY1NTUzNTUxMzYi_pc"  # Replace with your actual webhook URL

# Step 1: Fetch the web page
response = requests.get(source_url)
if response.status_code == 200:
    # Step 2: Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Extract specific elements (replace with actual selectors)
    title = soup.find("h1").get_text()  # Example selector for title
    description = soup.find("p").get_text()  # Example selector for description
    
    # Step 4: Prepare the data payload
    data = {
        "title": title,
        "description": description,
        "link": source_url
    }

    # Step 5: Send the data to Pabbly Webhook
    response = requests.post(webhook_url, json=data)
    if response.status_code == 200:
        print("Data sent successfully to Pabbly.")
    else:
        print("Failed to send data to Pabbly:", response.status_code)
else:
    print("Failed to fetch the page:", response.status_code)
