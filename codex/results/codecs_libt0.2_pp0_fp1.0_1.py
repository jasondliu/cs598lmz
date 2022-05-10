import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import os
import sys
import time
import datetime
import json
import re
import random
import string
import logging
import requests
import urllib
import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import http.client
import socket
import ssl
import threading
import queue
import traceback
import subprocess
import platform

from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.parse import urlunparse
from urllib.parse import urlencode
from urllib.parse import quote
from urllib.parse import unquote

from . import utils
from . import config
from . import log
from . import db
from . import db_redis
from . import db_mysql
from . import db_sqlite
from . import db_mongodb
from . import db_elastic
