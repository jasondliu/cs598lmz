import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import json
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def main():
    # get name/names of stock to look up
    stock = raw_input("Enter the stock symbol you would like information on: ")
    stock = stock.upper()

    # get the current price of the stock
    url = 'https://finance.yahoo.com/quote/' + stock + '?p=' + stock
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    price = soup.find(class_='My(6px) Pos(r) smartphone_Mt(6px)').find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').getText()
    print("Current price: " + price)

    # get the dividend information on the stock
    url = 'https://finance.
