import requests
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup



logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def IncomeTaxInfoFrom():
  logging.info("Entering to IncomeTaxInfoFrom")
  
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  driver = webdriver.Chrome(options=options)  # Or use webdriver.Firefox(), etc.

  # Open the URL
  url = "https://www.incometax.gov.in/iec/foportal/latest-news"
  driver.get(url)

  time.sleep(3)  # Allow the page to load

  all_news = []

  # while True:
  time.sleep(2)  # Wait for news items to load

  soup = BeautifulSoup(driver.page_source,'html.parser')
  news_items = soup.find_all('div',class_="views-row")

  logging.info(f"news_items-{news_items}")
  for item in news_items:
    # logging.info(f"item{item}")
    try:
        
        date = item.find('div',class_="up-date").get_text()
        title = item.find('div', class_="d-flex gry-ft").find('p').get_text(strip=True)
        logging.info(" ")
        logging.info(f"Updated Date-{date} Updated Rules--{title}")
        logging.info(" ")
    except Exception as e:
        print("Error extracting one item:", e)

  driver.quit()

  



# IncomeTaxInfoFrom()


def IncomeTaxInfoByRequestMethod():
  logging.info("Entering To IncomeTaxInfoByRequestMethod")
  url = 'https://www.incometax.gov.in/iec/foportal/latest-news'
  res = requests.get(url)
  if res.status_code == 200:
    soup = BeautifulSoup(res.text,'html.parser')
    logging.info(f"soup{soup}")
    all_list = soup.find_all('div',class_='views-row')
    count = 0 
    for item in all_list:
      # print(count+1)
      # logging.info(item)
      date = item.find('div',class_='up-date').text
      rules = item.find('p').get_text(strip=True)
      print(f"{count+1}.Upadted Date-{date}\n{rules}")
      count =count + 1
  else:
    logging.info(f"status Code ---{res.status_code}")


IncomeTaxInfoByRequestMethod()
