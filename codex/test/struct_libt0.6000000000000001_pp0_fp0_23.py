import _struct
import time
import csv
import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from os import path
from os import walk
from os import remove
from os import mkdir
from os import listdir

# CONSTANTS
A_DIR = 'A'
B_DIR = 'B'
LIVE_DIR = 'live'

# GLOBALS
A_PATH = ""
B_PATH = ""
LIVE_PATH = ""

A_FILE_LIST = []
B_FILE_LIST = []
LIVE_FILE_LIST = []

A_FILE_COUNT = 0
B_FILE_COUNT = 0
LIVE_FILE_COUNT = 0

A_DIR_COUNT = 0
B_DIR_COUNT = 0
LIVE_DIR_COUNT = 0

A_DATETIME = ""
B_DATETIME = ""
LIVE_DATETIME = ""

A_SIZE = 0
B_SIZE = 0
LIVE_SIZE = 0

LOG_
