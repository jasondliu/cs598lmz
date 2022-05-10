import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QEventLoop
from PyQt5.QtWebEngineWidgets import QWebEngineView

from time import sleep
import pyautogui as m
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from threading import Thread
import threading

URL = "https://www.facebook.com/ads/manager/accounts/account/campaigns"

class Ui_Facebook(object):
    def __init__(self):

        self.options = Options()
        # self.options.add_argument("--disable-gpu")
        # self
