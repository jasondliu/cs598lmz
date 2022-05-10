import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

import sys
import time
import datetime
import calendar
import requests
from bs4 import BeautifulSoup
import re
import json
from pymongo import MongoClient

# Needed for Python 2.7
reload(sys)
sys.setdefaultencoding("utf-8")

# Config
BASE_URL = 'https://www.indeed.com'
SEARCH_URL = 'https://www.indeed.com/jobs?q=software+engineer&l=Seattle%2C+WA&radius=0'
#SEARCH_URL = 'https://www.indeed.com/jobs?q=software+engineer&l=Seattle%2C+WA&radius=0&start={}'

# Scrape a single job
def scrape_job(job):
    #print job.prettify()
    title = job.find('a', {'class': 'jobtitle'})
    company = job.find('span', {'class
