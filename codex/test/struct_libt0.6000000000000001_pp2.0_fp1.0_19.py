import _struct
import time
import socket
import os
import math
import random
import sys
import traceback
import base64

if sys.version_info[0] < 3:
    import httplib
    import urllib
    import urllib2
    import cookielib
else:
    import http.client as httplib
    import urllib.request, urllib.parse
    import urllib.request as urllib2
    import http.cookiejar as cookielib

class XunleiLixianAPI(object):
    """
    XunleiLixianAPI implements the Xunlei lixian api.
    """
    def __init__(self, username, password, cookie_path=None):
        self.username = username
        self.password = password
        self.cookie_path = cookie_path
        self.cookie = None
        self.user_id = None
        if cookie_path:
            self.load_cookie()
