import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n' + __import__('random').choice(['Mustard', 'Ketchup', 'Relish']) + '\n')).start()

# from bs4 import BeautifulSoup
# import requests
# import time
# import random
# import sys, threading
# from random import randint
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.chrome.options import Options
# import re
# import os
# import json
# import urllib
# import urllib.request
# import argparse
#
