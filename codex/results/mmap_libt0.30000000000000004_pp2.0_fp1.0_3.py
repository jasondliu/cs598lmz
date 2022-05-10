import mmap
import os
import re
import sys
import time
import traceback

from . import constants
from . import errors
from . import utils
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_re_kv = re.compile(r'^([^=]+)=(.*)$')
_re_kv_list = re.compile(r'^([^=]+)=(.*)$')
_re_kv_list_split = re.compile(r'[,;]')
_re_kv_list_split_space = re.compile(r'[\s,;]')
_re_kv_list_split_space_quote = re.compile(r'[\s,;"]')
_re_kv_list_split_space_quote_escape = re.compile(r'[\s,;"\\]')
_re_kv_list_split_space_quote_escape_bracket = re.compile(r'[\s
