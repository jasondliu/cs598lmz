import bz2
bz2.compress('my data to compress')

import json
json.dumps([1, 'simple', 'list'])

from urllib.request import urlopen
from io import BytesIO
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import re

from tkinter import Tk, Label, Button
from tkinter.filedialog import askopenfilename

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from scrapy.conf import settings
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy import log
from scrapy.shell import inspect_response

from urllib import parse
from datetime import datetime
import scrapy
import os
import re
import json
import pandas


settings = {
        'FILES_STORE':
