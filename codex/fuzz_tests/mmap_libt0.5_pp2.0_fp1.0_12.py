import mmap
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from multiprocessing import Process
from threading import Thread
from typing import List, Tuple

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common import *
from config import Config
from db import *
from utils import *

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select


class PrecheckThread(Thread):
    def __init__(self, config: Config, db: Database, driver: webdriver):
        super().__init__()
        self.config = config
        self.
