import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import os
import re
import sys
import time
import datetime
import logging
import argparse
import subprocess
import collections
import threading
import multiprocessing
import traceback

import requests
from bs4 import BeautifulSoup

from utils import *

#-------------------------------------------------------------------------------
# Global Variables
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Classes
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Crawler')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output')
    parser.add_argument('-d', '--debug', action='store_true', help='debug output')
    parser.add_argument('-t', '--test', action='store_true', help='test')
    parser.add_argument
