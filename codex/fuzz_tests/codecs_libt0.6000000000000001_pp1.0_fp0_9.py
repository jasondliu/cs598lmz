import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

##TODO:
##    1. Get the text from the webpage.
##    2. Save it to a text file.

import requests
from bs4 import BeautifulSoup

def get_html(url):
    ##TODO:
    ##    1. Use requests library to get the content from the url.
    ##    2. Return the text content.
    html = requests.get(url)
    return html.text

def get_html_bs(url):
    ##TODO:
    ##    1. Use requests library to get the content from the url.
    ##    2. Create a BeautifulSoup object with the returned text.
    ##    3. Return the BeautifulSoup object.
    html = requests.get(url)
    html.encoding = 'utf-8'
    bs = BeautifulSoup(html.text, 'html.parser')
    return bs

def get_text(html_bs):
    ##
