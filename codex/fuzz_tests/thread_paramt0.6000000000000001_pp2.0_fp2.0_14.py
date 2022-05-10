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

def get_domain(url):
    # regex = r"(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|
