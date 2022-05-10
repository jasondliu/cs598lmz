import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

import sys
import re
import os
import time
import json
import csv
import codecs
import shutil
import requests
import datetime
import traceback
import subprocess
import urllib
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.parse import quote
from urllib.parse import unquote
from urllib.parse import urlencode
from urllib.request import urlretrieve
from urllib.request import urlopen
from urllib.request import Request
from urllib.request import build_opener
from urllib.request import HTTPCookieProcessor
from urllib.request import install_opener
from urllib.request import ProxyHandler
from urllib.request import HTTPHandler
from urllib.request import HTTPSHandler
from urllib.request import HTTPRedirectHandler
from urllib.request import HTT
