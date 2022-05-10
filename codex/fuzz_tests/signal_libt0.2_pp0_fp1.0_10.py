import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtCore import QTimer

from PyQt5.QtCore import QEventLoop
from PyQt5.QtCore import QUrl
from PyQt5.QtNetwork import QNetworkAccessManager
from PyQt5.QtNetwork import QNetworkRequest

import sys
import time
import json
import os
import re
import requests
import urllib
import urllib.request
import urllib.parse
import urllib.error
import base64
import hashlib
import rsa
import binascii
import random
import string
import http.cookiejar
import codecs
import json
import threading
import queue

from bs4 import BeautifulSoup

from weibo_login import WeiboLogin

class WeiboCrawler
