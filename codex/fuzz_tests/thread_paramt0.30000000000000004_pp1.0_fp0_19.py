import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import time
import re
import sys
import json
import math
import random
import requests
import argparse
import traceback
import threading
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def parse_args():
    parser = argparse.ArgumentParser(description='Instagram Bot')
    parser.add_argument('-u', '--username', help='Instagram username', required=True)
    parser.add_argument('-p', '--password', help='Instagram password', required=True)
    parser.
