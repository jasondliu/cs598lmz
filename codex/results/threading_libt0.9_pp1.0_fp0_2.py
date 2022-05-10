import threading
threading.currentThread().getName()
myName = threading.currentThread().getName()

#import csv
# Class for price capture
import re
import requests
import csv
from bs4 import BeautifulSoup

class priceCapture:
    def pre_process(self, site_url):
        # use requests to get html
        response = requests.get(site_url)
        # use bs4 to parse html
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
    def post_process(self, soup):
        return soup
    def run(self, soup):
        self.soup_pre = self.pre_process(self.url)
        self.soup = self.post_process(self.soup_pre)

        self.div_price = self.soup.find('div', class_='price')

        self.old_price = self.div_price.find('span', class_='old-price')
        self.new_price = self.div_price.find('span', class_='price')

       
