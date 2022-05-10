import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtWebKit import QWebSettings
from PyQt5 import QtCore

from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

from bs4 import BeautifulSoup
import sys
import urllib
import socket
import os
import re
import argparse
import json
import threading
import time
import datetime
import sqlite3
from collections import defaultdict
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
