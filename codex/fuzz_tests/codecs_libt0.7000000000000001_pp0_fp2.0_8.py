import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

from bs4 import BeautifulSoup
import requests
import re
import itertools
import os

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def main():
    print "Hello, world!"
    # with open('data/csv/stations.csv', 'rb') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         print row

# # #
