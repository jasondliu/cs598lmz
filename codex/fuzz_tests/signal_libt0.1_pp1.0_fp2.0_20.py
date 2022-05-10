import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtCore import QTimer

from PyQt5.QtCore import QEventLoop
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QTimer
from PyQt5.QtNetwork import QNetworkAccessManager
from PyQt5.QtNetwork import QNetworkRequest
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication

import sys
import time
import json
import re
import os
import requests
import random
import datetime
import traceback
import threading
import queue

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
