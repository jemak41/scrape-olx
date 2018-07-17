from bs4 import BeautifulSoup
from selenium import webdriver
import re, os, requests, csv
from selenium.common.exceptions import NoSuchElementException
import getpass
import time

#For pageloading
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = input('Type the url: ')

'''
capa = DesiredCapabilities.CHROME
capa['pageLoadStrategy'] = 'none'
driver = webdriver.Chrome(desired_capabilities=capa)
wait = WebDriverWait(driver, 20)
driver.get(url)
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@aria-label='Next page']")))
driver.execute_script("window.stop();")
'''

driver = webdriver.Chrome()
driver.get(url)

page = 1
pages = 10

source = driver.page_source
soup = BeautifulSoup(source, 'lxml')

product = []
price = []
location = []
pro = ''

while page < pages:
    for i in soup.find_all('div', class_='item'):
        try:
            if i.find('span', class_ = 'title' ).text == None or i.find('span', class_ = 'price' ).text == None or i.find('span', class_='location').text == None:
                pass
            else:
                product.append(i.find('span', class_ = 'title' ).text)
                price.append(i.find('span', class_ = 'price' ).text)
                loc = (i.find('span', class_='location').text).strip()
                location.append(loc)
        except:
            pass
    page += 3

    try:
        #time.sleep(2)
        button = driver.find_element_by_xpath("//a[@aria-label='Next page']")
            #driver.find_element_by_xpath("//input[@type='submit']")
            #driver.find('li', class_='pagination-next')
        button.click()
        source = driver.page_source
        soup = BeautifulSoup(source, 'lxml')
    except NoSuchElementException:
        break

for p in range(len(product)):
    print(product[p] + ', ' + price[p] + ',' + location[p] )
