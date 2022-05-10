import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#If you get this error: "ImportError: DLL load failed: The specified procedure could not be found,"
# try:
#     from ctypes import wintypes
#     from ctypes.wintypes import * # pyinstaller seems to not pick this up for some reason
#     ctypes.windll.kernel32.SetConsoleTitleW.argtypes = [wintypes.LPCWSTR]
#     ctypes.windll.kernel32.SetConsoleTitleW.restype = wintypes.BOOL
# except:
#     pass

import time
import os
import time as time
from datetime import date
import requests
from tqdm import tqdm
import bs4
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import json
from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.
