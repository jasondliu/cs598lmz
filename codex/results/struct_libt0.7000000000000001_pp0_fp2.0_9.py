import _struct
import ctypes
import ctypes.util
import itertools
import os
import posixpath
import re
import stat
import sys
import tempfile
import threading

import cython
import cython.operator

from . import __version__
from . import exception
from . import pyximport
from . import pyimport
from . import utils
from . import py3compat
from .compat import basestring, bytebuffer, bytes, integer_types, PY2, PY3, StringIO, _str, _unicode
from .deprecation import warn


if PY3:
    unicode = str

try:
    from functools import lru_cache
except ImportError:
    from .utils import lru_cache


API = None
API_tag = None

_cached_test_function = None

_cached_pyx_files = {}

_cached_pyx_file_dicts = {}

_cached_pyx_source_bytes = {}

_cached_pyx_source_dict
