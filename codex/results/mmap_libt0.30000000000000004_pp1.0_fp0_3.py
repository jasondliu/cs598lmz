import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib
import zipfile

import requests

import config
import utils

# Set up logging
logger = logging.getLogger(__name__)

# Set up requests session
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'})

# Set up regexes
re_file = re.compile(r'^(?P<path>[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/[^/]+/
