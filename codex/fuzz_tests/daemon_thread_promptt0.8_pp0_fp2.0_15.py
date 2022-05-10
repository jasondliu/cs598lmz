import threading
# Test threading daemonic
import time
from asyncio.windows_utils import socketpair
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.expected_conditions import\
    visibility_of_element_located, \
    text_to_be_present_in_element

from selenium import webdriver
from pyvirtualdisplay import Display  # if you are using virtual display, install this package
import subprocess
import datetime
import sys
import logging
import os
import command_executor

import config_parser
import utils

logger = logging.getLogger(__name__)

class State:
    def __init__(self):
        self.isVideoReady = False
        self.isVideoPlaying = False
        self.isStart = False
        self.isEnd = False
        self.isVideoError = False
