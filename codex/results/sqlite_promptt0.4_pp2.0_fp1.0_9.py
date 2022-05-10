import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import time

import app
import config
import db
import dl
import log
import util

logger = log.get_logger()

#
#
#

class Downloader:
    def __init__(self, config):
        self.config = config
        self.downloader = dl.Downloader(config)

    def download(self, url):
        return self.downloader.download(url)

    def download_to_file(self, url, filename):
        return self.downloader.download_to_file(url, filename)

#
#
#

class DownloaderThread(threading.Thread):
    def __init__(self, downloader, url, filename):
        threading.Thread.__init__(self)

        self.downloader = downloader
        self.url = url
        self.filename = filename
        self.result = None

    def run(self):
        self.result = self.downloader.download_to_file(self.url, self.filename)

#
#
