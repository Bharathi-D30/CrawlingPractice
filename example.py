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
        text = quote.find("span", class_="text").get_text()

        author = quote.find("small", class_="author").get_text()
    logging.info("               ")
    logging.info("               ")
    logging.info("               ")
    logging.info("               ")
    logging.info(f"one{one}")
    logging.info("               ")
    logging.info("               ")
    logging.info("               ")


    print(f"{text} — {author}")


# crawlingfunction()







def scrape_news_headlines():
    logging.info("Entering to scrape_news_headlines::::::::")
    url = "https://www.thehindu.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # raise error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching news site: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find headlines - adjust based on structure
    headlines = soup.find_all("h1", class_="title") 
    logging.info(f"headlines{headlines}") # Example class

    print("Top News Headlines:\n")
    for idx, headline in enumerate(headlines[:10], start=1):  # Just top 10
        logging.info(f"headline{headline}")
        logging.info(f"idx{idx}")
        title = headline.find('a').get_text(strip=True)
        # link = headline.get('href')
        print(f"{idx}. {title}")
        # print(f"   Link: {link}\n")



scrape_news_headlines()





