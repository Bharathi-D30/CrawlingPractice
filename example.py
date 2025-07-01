import logging
import requests
from bs4 import BeautifulSoup
import json



# Enable logging to show INFO level messages
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


print("Hello world")


def crawlingfunction():
    logging.info("entering to crawlingfunction")

    # Simple URL to scrape
    url = "https://quotes.toscrape.com"

    response = requests.get(url)
    # parsejons = json.loads(response)
    # logging.info(f'parsejons:::::{parsejons}')
    soup = BeautifulSoup(response.text, 'html.parser')
    # logging.info(f"soup::::{soup}")
    # Scrape all quotes from the page
    quotes = soup.find_all("div", class_="quote")
    # logging.info(f'quotes{quotes}')
    text = " "
    author = " "
    for quote in quotes:
        one = quote
        logging.info("entering to loop")
        text += quote.find("span", class_="text").get_text()

        author += quote.find("small", class_="author").get_text()
    logging.info("               ")
    logging.info("               ")
    logging.info("               ")
    logging.info("               ")
    logging.info(f"one{one}")
    logging.info("               ")
    logging.info("               ")
    logging.info("               ")


    print(f"{text} — {author}")


crawlingfunction()
