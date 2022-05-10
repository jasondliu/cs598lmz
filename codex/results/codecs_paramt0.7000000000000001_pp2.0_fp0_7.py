import codecs
codecs.register_error('surrogate_or_unknown', surrogates_or_unknown)

import os
import sys
import json
import shutil
import logging
from urllib import request, parse
from http import HTTPStatus
from contextlib import contextmanager
from datetime import datetime
from argparse import ArgumentParser
from collections import namedtuple
from functools import partial
from urllib.error import HTTPError

from jinja2 import Environment, FileSystemLoader
from yaml import safe_load

from . import __version__
from .exceptions import CmdError, CmdValueError, CmdArgumentError, TemplateError

logger = logging.getLogger(__name__)

# Constants

SYS_ENCODING = sys.getdefaultencoding()
SYS_IS_WIN = sys.platform.startswith('win')
CONFIG_NAME = 'conf.yml'

# Types

Error = namedtuple('Error', 'code message')

# Functions

def check_file_exists(file_name, msg=None):
    if not os
