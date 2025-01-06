import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "http://quotes.toscrape.com"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all quote elements
    quotes = soup.find_all("div", class_="quote")
    
    # Extract and print the text of each quote
    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        print(f"Quote: {text}\nAuthor: {author}\n")
else:
    print("Failed to retrieve the web page.")
