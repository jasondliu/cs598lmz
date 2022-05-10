import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, shutil
from selenium.webdriver.common.action_chains import ActionChains
import re
import time
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from PIL import Image
import pytesseract
from io import BytesIO
import xlwt
import xlrd
from xlutils.copy import copy as xl_copy
import datetime
import sys
import getopt
import traceback
import json
import csv
from random import randint
import multiprocessing
from multiprocessing import Pool
from multipro
