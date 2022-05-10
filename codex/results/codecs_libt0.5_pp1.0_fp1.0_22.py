import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
import sys
import time
import datetime
import os
import re
import csv
import traceback
import random
import string
import subprocess
import argparse
import json
import logging
import logging.handlers
import logging.config
import logging.config
import requests
import sqlite3
import pandas as pd
import pprint as pp
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.common.ex
