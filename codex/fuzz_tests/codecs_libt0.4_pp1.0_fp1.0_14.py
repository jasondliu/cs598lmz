import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# import django
# django.setup()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

from time import sleep
import re

from random import randint

import datetime

from multiprocessing import Pool

from django.db import close_old_connections

from django.db import connection

from django.core.exceptions import ObjectDoesNotExist

from django.db import transaction
from django.db.models import F

from django.db.models import Max
from django.db.models
