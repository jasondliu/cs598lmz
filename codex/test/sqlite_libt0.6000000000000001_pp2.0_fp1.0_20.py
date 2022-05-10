import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import shutil
import logging
import json
import time
import random
import platform
import configparser
import traceback

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from urllib.parse import urlparse, parse_qsl

import util
import baiducloud
import qiniuyun

# 这个类用于处理HTTP请求
class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info('[%s] "%s"' % (self.client_address[0], self.requestline))
        begin = time.time()
        # 解析请求的路径
        query = urlparse(self.path).query
        # 解析请求的参数
        params = dict(parse_qsl(query))
        # 获取请求的参数
        action = params
