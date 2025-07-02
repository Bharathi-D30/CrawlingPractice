import logging
from selenium import webdriver
import time
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
    logging.info(f"one{one}")
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



# scrape_news_headlines()


def getVegAndPrice():
    logging.info("Entering to getVegAndPrice")
    try:
        # url = 'https://www.livechennai.com/Vegetable_price_chennai.asp'
        # res = requests.get(url)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # run in background
        driver = webdriver.Chrome(options=options)

        url = 'https://www.livechennai.com/Vegetable_price_chennai.asp'
        driver.get(url)
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source,'html.parser')
        driver.quit()
        # logging.info(f'soup{soup}')


        table = soup.find("table", class_="table table-bordered table-striped gold-rates")
        if not table:
            logging.warning("Vegetable price table not found.")
            return

        listTable = table.find_all('tr')[2:]



        for row in listTable:
            allcol = row.find_all('td')
            # logging.info(f'allcol:{allcol}')
            vegName = allcol[1].text
            vegPrice = allcol[2].text

            print(f'{vegName}₹{vegPrice}')

    except Exception as e:
        print(f"Error: {e}")











getVegAndPrice()




  
