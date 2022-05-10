import mmap
import os
import re
import signal
import sys
import time
import traceback

from selenium.common.exceptions import (
    ElementNotInteractableException,
    ElementNotVisibleException,
    InvalidArgumentException,
    InvalidSelectorException,
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from . import __version__

LOGGER.setLevel(logging.WARNING)

# This is a workaround for a bug in selenium
# https://github.com/SeleniumHQ/selenium/issues/5193
# https://github.com/SeleniumHQ/sel
