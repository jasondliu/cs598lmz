import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.proxy import Proxy, ProxyType

#_______________________________________________________________________________
def main():
	txtfile = open("links.txt", "r") 
	links = txtfile.read().split('\n')
	txtfile.close()
	
	PROXY = "proxy.crawlera.com:8010" # IP:PORT or HOST:PORT

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--proxy-server=%s' % PROXY)
	browser = webdriver.Chrome(chrome_
