import mmap
import os
import re
import sys

from . import _compat
from . import _util
from . import _winreg

# The following are used to build the list of files to be scanned.
_FILE_EXTENSIONS = ['.exe', '.dll', '.ocx', '.cpl', '.sys', '.drv', '.scr']
_FILE_EXTENSIONS_REGEX = re.compile(r'\.(exe|dll|ocx|cpl|sys|drv|scr)$', re.I)
_FILE_EXTENSIONS_REGEX_DOT = re.compile(r'\.(exe|dll|ocx|cpl|sys|drv|scr)\.$', re.I)
_FILE_EXTENSIONS_REGEX_DOT_DOT = re.compile(r'\.(exe|dll|ocx|cpl|sys|drv|scr)\.\.$', re.I)
_FILE_EXTENSIONS_REGEX_DOT_DOT_DOT = re.compile(r'\.(exe
