import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from bs4 import BeautifulSoup

from . import common
from . import config
from . import constants
from . import database
from . import exceptions
from . import log
from . import util
from . import webutil

class Web(object):
    """
    The Web class is responsible for downloading web pages and parsing them.
    """

    def __init__(self, config_dir, database_dir, data_dir, cache_dir,
                 download_dir, download_delay, download_retries,
                 download_timeout, ignore_robots_txt,
                 user_agent, proxy_server, proxy_type, proxy_authentication,
                 proxy_username, proxy_password,
                 no_cache, clear_cache, clear_downloads,
                 clear_database, clear_data,
                 clear_all,
                 debug, verbose, quiet,
                 log_dir, log_level, log_interval,
                 log_verbose,
