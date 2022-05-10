import lzma
lzma.decompress(req.content).decode('utf-8')

#BeautifulSoup
from bs4 import BeautifulSoup
parsed = BeautifulSoup(req.content, 'html.parser')
# print(parsed.prettify())

#findAll
titles = parsed.find_all('a')
titles[0].get_text()

#for 
for i in titles:
    print(i.get_text())

#find class
titles = parsed.find_all(class_='ticker')
for i in titles:
    print(i.get_text())

#tik tok
#Define
#import
#request
#pass request to BeautifulSoup

#Calling API
import requests
import json
url = 'https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json'
req = requests.get(url=url)
parsed = json.loads(req.text)
# print(parsed)

#Calling API

