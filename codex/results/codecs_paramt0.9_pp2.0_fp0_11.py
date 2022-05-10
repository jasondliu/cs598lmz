import codecs
codecs.register_error("strict", codecs.replace_errors)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


l = open("link.txt","r")
password = l.readline().split("\"")[1]
#password = ''

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://en.wikipedia.org/wiki/List_of_Jeopardy%21_tournaments_and_events')
soup = BeautifulSoup(driver.page_source,"lxml")

data = soup.find('table',id='toc')
all_urls = data.find_all('a')

links = []

for url in all_urls:
    links.append(url['href'])
links.pop(0)


base_url = "https://en.wikipedia.org"
start = '/wiki/2010_Jeopardy!_One_
