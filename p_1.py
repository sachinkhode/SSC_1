from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pymongo import MongoClient
db22 = MongoClient().mydb22

ssc_ppr =db22['ssc_ppr']

chrome_options = Options()
ssc = {}
driver = webdriver.Chrome(executable_path='C:\\Users\\syss\\Desktop\\chromedriver',chrome_options= chrome_options)

driver.maximize_window()

driver.get('https://cracku.in/ssc-cgl-previous-papers')

time.sleep(2)

for i in range(1,112):
    listing = driver.find_elements_by_xpath("//*[@id='mocks-list']/div[2]/table/tbody/tr["+str(i)+"]/td[2]/a[1]")
    print(listing)

