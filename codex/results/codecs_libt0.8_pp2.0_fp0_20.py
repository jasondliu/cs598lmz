import codecs
codecs.open('test.html', 'r', 'utf-8').read()

# HTMLParser

import html.parser
p = html.parser.HTMLParser()
p.feed('<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>')

# Beautiful Soup

from bs4 import BeautifulSoup
soup = BeautifulSoup('<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>', 'lxml')
soup.find('h1')

soup = BeautifulSoup(html, 'lxml')
soup.find('div', {'class': 'title'})
soup.find_all('div', {'class': 'title'})

# lxml

html = requests.get('http://python.org/').text
tree = lxml.html.fromstring(html)
tree.cssselect('div.title')

# CSS选择器

import requests
r = requests.
