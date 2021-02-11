# -*- coding: utf-8 -*-
"""
Created on Web Nov 11 12:24:54 2020

Google Appstore Review Crawling

@author: jaewoong Han
"""

# package load
import pandas as pd
import requests
from selenium import webdriver
import time
import random
from tqdm import tqdm
import requests
#pip install request
#pip install beautifulsoup4
from bs4 import BeautifulSoup

# cite load & search keywords
#driver load
driver = webdriver.Chrome('./data\\chromedriver.exe')

#url.get
url="https://play.google.com/store"
driver.get(url)

#keyword_list
searchText_T = ["심쿵","위피", "아만다", "글램", "당연시", "정오의 데이트"]

driver.find_element_by_xpath('//*[@id="gbqfq"]').send_keys(searchText_T[0])
driver.find_element_by_xpath('//*[@id="gbqfb"]/span').click()
driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/c-wiz/c-wiz[1]/c-wiz/div/div[2]/div[1]/c-wiz/div/div/div[2]/div/div/div[1]/div/div/div[1]/a/div').click()
driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div/main/div/div[1]/div[6]/div/span/span').click()

# 무한 스크롤
import time

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")         

while True:

    # Scroll down to bottom                                                      
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)                                                
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")  
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height            
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:                                                
        driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div/main/div/div[1]/div[2]/div[2]/div/span/span').click()

    last_height = new_height

# 에러나올경우
SCROLL_PAUSE_TIME = 1.5
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # (1) 4번의  스크롤링
    for i in range(4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

    # (2) 더보기 클릭
    driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
    
    # (3) 종료 조건
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 데이터 수집

# 파싱
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

# 별점
stars = driver.find_elements_by_xpath("//span[@class='nt2C1d']/div[@class='pf5lIe']/div[@role='img']")
# star.get_attribute('aria-label')

# 날짜
dates = driver.find_elements_by_xpath("//span[@class='p2TkOb']")
# date.text

# 리뷰
reviews = driver.find_elements_by_xpath("//span[@jsname='bN97Pc']")
# review.text
# len(reviews)

# 모두 수집
res_dict = []
for i in range(len(reviews)):
    res_dict.append({
        'DATE' : dates[i].text,
        'STAR' : stars[i].get_attribute('aria-label'),
        'REVIEW' : reviews[i].text
    })
    
res_df = pd.DataFrame(res_dict)

# 저장
res_df.to_excel('심쿵.xlsx')







    
    



