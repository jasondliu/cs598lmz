import codecs
codecs.register_error('strict', codecs.ignore_errors)

from io import BytesIO
from os.path import isfile, dirname, join as pjoin, realpath
from os import listdir
from hashlib import md5
from time import time
from datetime import datetime
from urllib.parse import urljoin, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from socket import error as SocketError
from html.parser import HTMLParser
from json import loads, dumps
from tempfile import NamedTemporaryFile, TemporaryDirectory
from subprocess import Popen, PIPE, STDOUT
from shutil import rmtree

from .utils import (
    get_config,
    get_logger,
    get_cache_dir,
    get_cache_file,
    get_cache_path,
    get_cache_url,
    get_cache_key,
    get_cache_info,
    get_cache_expire,
    get_cache_content,
    get_cache_headers,
   
