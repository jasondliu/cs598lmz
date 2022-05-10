import codecs
codecs.register_error("strict", codecs.ignore_errors)
import glob
import traceback
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
from csv_reader import *
from csv_writer import *

import mechanicalsoup
import requests
#from urllib.parse import urlparse

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


# in case of an error, return the tuple (None, None, None, error)
def parse_single_log(driver, url, soup, url_cleanse, pms, pms_repetition_in_url):
	#from urllib.parse import urlparse
	
	# if url does not start with "http", return (None, None, None, None)
	if not url.startswith('http'):
		return (None, None, None, None)

	if soup == None:
		return (None, None, None, None)
	
	pm_name_from_url = None
	pm_name
