import socket
import urllib.request
from bs4 import BeautifulSoup
from pymongo import MongoClient


mongo_client = MongoClient('127.0.0.1', 27017)
db = mongo_client.dbsparta 

driver = webdriver.Chrome('./chromedriver.exe')

option = webdriver.ChromeOptions()
option.add_argument('window-size=1920x1080')

driver.get('https://www.melon.com/chart/index.htm')


#크롬드라이브 안에 있는 것을 찾아주기 위해서
driver.switch_to_frame(driver.find_element_by_name('frame'))

#일단 클릭을 기다리는 시간이 필요할 듯 해서
