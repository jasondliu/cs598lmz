import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

import errno
import collections

import tkinter as tk

import pycurl
import io

class PyCurlResponse(object):
    """
    An object to hold response information.
    """
    def __init__(self):
        self.header = io.BytesIO()
        self.body = io.BytesIO()
        self.http_code = -1
        self.content_type = None
        self.url = None
        self.effective_url = None
        self.headers = {}
        self.history = []
        self.error = None
        self.proxies = []


def get_ngrok_info(url):
    connection = PyCurlResponse()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
