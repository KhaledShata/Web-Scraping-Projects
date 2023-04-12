from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd



# For Scheduling Scipt
from datetime import datetime
import os
import sys

# Place Where You Want the Csv File Saved After the Script Run
app_path = "E:\Python Projects\WebScraping\TheSunNews"

now = datetime.now()
day_month_year = now.strftime("%d%m%Y")


#Headless mode
options = Options()
options.headless = True




website = 'https://www.thesun.co.uk/'
path =r'C:\Users\dell\chromedriver'
service = Service(exectuable_path = path)


driver = webdriver.Chrome(service = service ,options = options)
driver.get(website)




# XPATH : //div[@class="teaser__copy-container"]
# Contain All News Boxes in The Sun Website
containers = driver.find_elements(by='xpath' ,value='//div[@class="teaser__copy-container"]')


news_info = []

#For Every New Box
for c in containers:

    #you can write . for shortcut
    title = c.find_element(by='xpath' , value = './a/h3').text

    subtitle =  c.find_element(by='xpath' , value = './a/p').text

    link = c.find_element(by='xpath' , value = './a').get_attribute("href")

    info = {"Title":title , "Subtitle":subtitle , "Link":link}
    news_info.append(info)




df = pd.DataFrame(news_info)
df.to_csv(f"{app_path}/Headline {day_month_year}.csv")
driver.quit()






