import socket
import sys
import threading
import time
import traceback
import urllib.request
from collections import deque
from datetime import datetime
from pathlib import Path
from queue import Queue
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

from src.utils import get_logger, get_config

logger = get_logger(__name__)

config = get_config()

# Global variables
NUM_WORKERS = config['crawler']['num_workers']
MAX_PAGES = config['crawler']['max_pages']
MAX_DEPTH = config['crawler']['max_depth']
MAX_QUEUE_SIZE = config['crawler']['max_queue_size']

# Queue of links to be crawled
new_urls = Queue()

# Queue of links that have been crawled
processed_urls = set()

# Queue of links that have been crawled
error_urls = set()

# Que
