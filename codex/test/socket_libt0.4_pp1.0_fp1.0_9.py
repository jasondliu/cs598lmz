import socket
import sys
import time
import urllib
import urllib2
import urlparse

from bs4 import BeautifulSoup
from Queue import Queue
from threading import Thread

from . import utils
from .models import *

class Crawler(Thread):
    def __init__(self, url, queue, max_depth, max_pages, verbose):
        Thread.__init__(self)
        self.url = url
        self.queue = queue
        self.max_depth = max_depth
        self.max_pages = max_pages
        self.verbose = verbose

    def run(self):
        self.crawl(self.url, 0)

    def crawl(self, url, depth):
        if depth > self.max_depth:
            return

        if self.max_pages > 0 and self.queue.qsize() > self.max_pages:
            return

