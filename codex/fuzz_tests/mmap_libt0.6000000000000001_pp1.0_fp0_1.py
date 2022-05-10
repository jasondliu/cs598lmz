import mmap
import os
import re
import shutil
import sys
import tempfile
import time
import xml.etree.ElementTree as ET
import zipfile

from collections import OrderedDict
from itertools import chain
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from . import __version__
from .common import (
    __version__,
    _t,
    ARCHIVE_EXTS,
    ARCHIVE_MIMES,
    ARCHIVE_PAT,
    DATE_PAT,
    DATE_TZ_PAT,
    DATETIME_PAT,
    DATETIME_TZ_PAT,
    DECIMAL_PAT,
    FLOAT_PAT,
    HASH_PAT,
    INTEGER_PAT,
    IPV4_PAT,
    IPV6_PAT,
    ISO8601_PAT,
    ISO8601_TZ_PAT,

