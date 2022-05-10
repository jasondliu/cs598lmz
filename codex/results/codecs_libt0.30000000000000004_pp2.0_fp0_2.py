import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import re
import os
import sys
import csv
import json
import time
import random
import socket
import datetime
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import quote
from urllib.parse import unquote
from urllib.parse import urlparse
from urllib.parse import parse_qs
from urllib.parse import parse_qsl
from urllib.parse import urlencode
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from urllib.parse import urljoin
from urllib.parse import urldefrag
from urllib.parse import quote_plus
from urllib.parse import unquote_plus
from urllib.parse import quote_from_
