import mmap
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime

from urllib.parse import urlparse

from utils import *
from config import *
from db import *

def get_links(csv_file):
    """
    Returns a list with the links from the given csv file

    Args:
        csv_file (string): The path to the csv file
    """
    links = []

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            links.append(row[0])

    return links
