import sys, threading
threading.Thread(target=lambda: sys.stdout.flush()).start()
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
import requests
from PIL import Image
from glob import glob
from os import listdir
from os.path import isfile, join
import os
from pandas import DataFrame
from openpyxl import Workbook

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import WebDriverException


class WindowClass(QMainWindow):
    def __init__(self):
        super().__init
