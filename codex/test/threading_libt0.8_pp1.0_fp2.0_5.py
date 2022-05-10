import threading
threading.stack_size(67108864)

import pandas as pd
import numpy as np
from io import BytesIO
import re
import time
import requests

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# gspread
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# openpyxl
import openpyxl

# 로그인해서 들어가야 하는 페이지
main_url = 'https://www.hikorea.go.kr/pt/ptQaRmgsZzqcPop001.do'

# 대학 검색 결과 페이지
# 페이지네이션 
