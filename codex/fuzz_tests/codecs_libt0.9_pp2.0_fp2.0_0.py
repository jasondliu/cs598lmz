import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import requests
from pyexcel_xls import get_data
from bs4 import BeautifulSoup
import csv
import json
import time
# import youdao
import sys
import chardet
from os import listdir
from os.path import isfile, join
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains


import random
random_names = ['James','John','Robert','Michael','William','David','Richard','Charles','Joseph','Thomas','Christopher','Daniel','Paul','Mark','Donald','George','Kenneth','Steven','Edward','Brian','Ronald','Anthony','Kevin','Jason','Matthew','Gary','Timothy','Jose','Larry','Jeffrey','Frank','Scott','Eric','Stephen','Andrew','Raymond','Gregory','Joshua','Jerry','Dennis','Walter','Patrick','Peter','Harold','Douglas','Henry','
