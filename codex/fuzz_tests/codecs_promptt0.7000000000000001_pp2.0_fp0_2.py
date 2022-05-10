import codecs
# Test codecs.register_error('test', codecs.ignore_errors)

import os
import os.path
import copy

import logging
from logging import info, warning, error
from logging import debug as debug_log

import json

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

import re

from traceback import print_exc

import threading

from urlparse import urlparse, urlunparse, urljoin

from lxml import etree

from . import parser
from . import utils
from . import config
from . import html_utils
from . import utils
from . import downloader

from .http import urlopen
from . import http

from . import sync
from .sync import Lock

from . import db
from . import web
from . import db_web_sync

from . import download_queue
from . import download_manager


GENERAL_DATABASE_NAME = 'general.db'
WEB_DATABASE_NAME = 'web.db'


class
