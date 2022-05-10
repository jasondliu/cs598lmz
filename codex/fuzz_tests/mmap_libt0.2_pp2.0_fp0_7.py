import mmap
import os
import re
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from itertools import chain
from operator import itemgetter
from optparse import OptionParser
from os.path import abspath, basename, dirname, exists, isdir, isfile, join
from subprocess import Popen, PIPE
from tempfile import mkdtemp
from threading import Thread

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import get_lexer_for_filename, get_lexer_by_name
from pygments.util import ClassNotFound

from . import __version__
from .compat import (
    BytesIO,
    FileNotFoundError,
    PermissionError,
    PY3,
    StringIO,
    TextIOWrapper,
    WindowsError,
    is_string,
    iteritems,
    itervalues,
    open,
    range,
    str,
    text_type,
    xrange,
)

