import codecs
codecs.getwriter('utf-8')(sys.stdout)

from bs4 import BeautifulSoup
from lxml import etree

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# URL
url = 'https://www.dhl.de/de/privatkunden.html'
# url = 'https://www.dhl.de/de/privatkunden/pakete-empfangen/versand-nachverfolgen.html'

# start browser
driver = webdriver.Firefox()
driver.get(url)

# find textfield and send tracking number
elem = driver.find_element_by_css_selector('input[id="track-search-input"]')
elem.send_keys('3SZBV99R0017002894')

# find button and click it
elem = driver.find_element_by_css_selector('button[id="track-search-button"]')
