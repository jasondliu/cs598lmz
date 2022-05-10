import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#import ctypes  # An included library with Python install.   
#ctypes.windll.user32.MessageBoxW(0, u"Your text", u"Your title", 1)
import urllib
from bs4 import BeautifulSoup
import re
quote_page = 'https://www.bloomberg.com/quote/SPX:IND'
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text
print (name)

price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print (price)

import ctypes  # An included library with Python install.   
ctypes.windll.user32.MessageBoxW(0, name, price, 1)

import tkinter as tk

