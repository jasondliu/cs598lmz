import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello, world!\n")).start()

from threading import Thread
from queue import Queue
import requests
from bs4 import BeautifulSoup
from lxml import html
from urllib.parse import urljoin
import re
from pprint import pprint

