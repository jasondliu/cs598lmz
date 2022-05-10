import mmap
import os
import re
import sys

from . import util
from . import version
from . import xdg
from . import xdg_config
from . import xdg_data

from .util import (
    _,
    PY2,
    PY3,
    basestring,
    bytes,
    bytes_to_str,
    ensure_bytes,
    ensure_str,
    ensure_unicode,
    is_bytes,
    is_str,
    is_unicode,
    str_to_bytes,
    unicode,
    unicode_to_str,
)

if PY2:
    from io import BytesIO as StringIO
else:
    from io import StringIO

if PY3:
    from configparser import ConfigParser, NoOptionError, NoSectionError
else:
    from ConfigParser import ConfigParser, NoOptionError, NoSectionError

__all__ = [
    "Config",
    "ConfigError",
    "ConfigParser",
    "NoOptionError",
    "NoSectionError
