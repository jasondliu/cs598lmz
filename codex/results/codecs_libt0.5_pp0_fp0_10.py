import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# 필요한 모듈을 불러온다.
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import re
import pandas as pd
from pandas import DataFrame

# 데이터 프레임을 생성한다.
columns = ['제목', '작성자', '조회수', '날짜']
df = DataFrame(columns=columns)

# 웹 드라이버를 이용해 크롬 브라우저를 실
