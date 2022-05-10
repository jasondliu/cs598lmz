import ctypes
import ctypes.util
import threading
import sqlite3
import os
import re
import sys

import abrt_p2_uploader
from abrt_p2_uploader.logger import logger
from abrt_p2_uploader.utils import get_p2_username, get_p2_password, \
    get_p2_url, get_p2_environment, get_p2_auth_type, get_p2_cookie_file, \
    get_p2_report_page_url, get_p2_max_retry, get_p2_retry_timeout

import pycurl

try:
    import pycurl.global_init
    pycurl.global_init(pycurl.GLOBAL_ALL)
except Exception:
    pass

NAME_MAXLEN = 32

libc = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)

# 64bit
CURLOPT_UPLOAD = 57
CURLOPT_READFUNCTION = 20012
