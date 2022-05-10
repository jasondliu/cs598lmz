import socket
import os
import sys
import time
import threading
import random
import string
import json
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.error import HTTPError
from socket import error as SocketError
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

# 全局使用的变量
# 全局使用的变量
# 全局使用的变量

# 扫描的目标
target = ''
# 扫描的目标端口
port = ''
#
