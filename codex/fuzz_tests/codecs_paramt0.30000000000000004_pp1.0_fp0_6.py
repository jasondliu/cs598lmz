import codecs
codecs.register_error('strict', codecs.ignore_errors)

import re
import os
import sys
import time
import json
import random
import logging
import argparse
import requests
import threading
import multiprocessing
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from collections import deque
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

# 全局变量
# 线程池
thread_pool = ThreadPoolExecutor(max_workers=10)
# 进程池
process_pool = ProcessPoolExecutor(max_workers=10)
# 目标url
target_url = None
# 线程锁
thread_lock = threading.Lock()

