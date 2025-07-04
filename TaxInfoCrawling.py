import requests
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



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


# IncomeTaxInfoByRequestMethod()


def MultipleUrlsNew():
  logging.info("Entering Into MultipleUrls Function")
  main_obj = []  # Should be a list to use append
  url = 'https://www.incometax.gov.in/iec/foportal/latest-news'
  next_button_url_href = ""  # start with empty string, not a space
  url_list = []
  count = 1
  flag = False

  while True:
      # Stop if URL already processed
      if next_button_url_href in url_list and next_button_url_href != "":
          break
      else:
          flag = True
          url_list.append(next_button_url_href)

      if flag:
          current_url = url + next_button_url_href
      else:
          current_url = url

      res = requests.get(current_url)
      soup = BeautifulSoup(res.text,'html.parser')
      all_item_list = soup.find_all('div',class_='views-row')
      # logging.info(f'soup{soup}')
      next_button = soup.find('li',class_='pager__item pager__item--next')
      # logging.info(f'next_button{next_button}')
      next_button_url = next_button.find('a')
      next_button_url_href = next_button_url['href']
      logging.info('next_button_url_href',next_button_url_href)
      for item in all_item_list:
        # print(count)
        date = item.find('div',class_='up-date').text
        rules = item.find('p').get_text(strip=True)
        # print(f"{count}.Upadted Date-{date}\n{rules}")

        main_obj.append({'count':count,'date':date,'rules':rules})
        count = count + 1

      # print('main_obj:', main_obj)
  
  for obj in main_obj:
    print(obj['count'],'Upadted Date'," ",obj['date'],'Rules'," ",obj['rules'])


    
    
# MultipleUrlsNew()



def BlogCrawling():
  logging.info("Entering to BlogCrawling Function")

  url = 'https://blog.saginfotech.com/india-first-nationwide-household-income-survey-2026-improve-tax-policy'
  res = requests.get(url)
  soup = BeautifulSoup(res.text,'html.parser')

  title = soup.find('h1',class_='page-title').get_text()
  print(f"=============={title}==============")
  content = soup.find('div',class_='entry-content')
  # print(content)
  if content:
    # Collect clean text parts
    full_text = ""
    for tag in content.find_all(True):  # True = all tags
        if tag.name in ['h1', 'h2', 'h3']:
            heading = tag.get_text(strip=True)
            full_text += f"\n\n=== {heading} ===\n" 
        elif tag.name == 'p':
            paragraph = tag.get_text(strip=True)
            full_text += f"{paragraph}\n"
        elif tag.name == 'li':
            list_item = tag.get_text(strip=True)
            full_text += f"- {list_item}\n"

    print(full_text)
  else:
    print("No content found.")

  # all_content = content.find_all('p')

  # for item in all_content:
  #   line_content = item.text
  #   print(line_content)
  #   print("\n")

  logging.info("Exiting From BlogCrawling Fucntion")
   

# BlogCrawling()


def ActsCrawling():
  logging.info("Entering to ActCrawling")

  options = webdriver.ChromeOptions()
  options.add_argument("--headless")
  options.add_argument("--log-level=3")
  driver = webdriver.Chrome(options=options)
  url = 'https://incometaxindia.gov.in/Pages/acts/index.aspx'

  driver.get(url)
  time.sleep(2)



  # soup = BeautifulSoup(driver.page_source,'html.parser')

  all_acts_div = driver.find_elements(By.CLASS_NAME,'search_result')
  print(f"Total Acts::{len(all_acts_div)}")

  for i,acts in enumerate(all_acts_div):
    Act = acts.find_element(By.CSS_SELECTOR,'.search_title a').text
    print(f"{i+1}.{Act}")

  driver.quit()

# ActsCrawling()


def ActsChapterList():
  logging.info(f"Entering to ActsChapterList::::::")
  options = webdriver.ChromeOptions()
  options.add_argument("--headless")
  driver = webdriver.Chrome(options=options)

  url = 'https://incometaxindia.gov.in/pages/acts/income-tax-act.aspx'

  driver.get(url)

  WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.TAG_NAME, "table"))
  )

  all_tables = driver.find_elements(By.TAG_NAME, 'table')

  for table in all_tables:
    try:
        # Check if the table has an id and ends with 'SearchParameters'
        table_id = table.get_attribute('id')
        if table_id and table_id.endswith('SearchParameters'):
            # Find all rows in the table
            rows = table.find_elements(By.TAG_NAME, 'tr')
            for row in rows:
                if 'Chapter Wise' in row.text:
                    # Find and click the radio button inside this row
                    radio_button = row.find_element(By.TAG_NAME, 'input')
                    logging.info(f"radio_button :::::::::::::::::::::{radio_button}")
                    radio_button.click()
                    # time.sleep(2)
                    
                    # time.sleep(2)
                    WebDriverWait(driver,10).until(
                      EC.presence_of_element_located((By.CLASS_NAME,'dt-pages-colls-2'))
                    )
                    logging.info("Clicked on 'Chapter Wise' option")
                    
                    main_div = driver.find_element(By.CLASS_NAME,'dt-pages-colls-2')
                    # logging.info(f"main_div  {main_div}")

                    chapter_list = main_div.find_elements(By.TAG_NAME , 'li')
                    for i,chapter in enumerate(chapter_list):
                      # logging.info(f"chapter   {chapter}")
                      try:
                          content = chapter.find_element(By.CLASS_NAME,'dt-ui-info-h1')
                          print(f"{i}. {content.text.strip()}")
                      except Exception as e:
                          logging.warning(f"Skipping chapter {i} due to missing span: {e}")



                      # Once clicked, exit loop
    except Exception as e:
        logging.warning(f"Error processing table: {e}")

    

  logging.info("Exiting from ActsChapterList Function")




ActsChapterList()




  
