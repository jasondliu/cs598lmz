import lzma
lzma.open

import os
import re
import sys
import time
import json
import shutil
import logging
import argparse
import subprocess

import requests
from bs4 import BeautifulSoup

from . import config
from . import utils
from . import logger
from . import exceptions
from . import constants
from . import __version__
from . import __author__
from . import __license__
from . import __url__
from . import __description__

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

class PypiDownloader(object):

    def __init__(self, package, version, dest, timeout=None,
                 retries=None, retry_delay=None, proxies=None,
                 insecure=False, quiet=False,
                 cache_dir=None, cache_ttl=None,
                 index_url=None, extra_index_url=None,
                 no_index=False, find_links=None,
                 session=None, platform=None, python_version
