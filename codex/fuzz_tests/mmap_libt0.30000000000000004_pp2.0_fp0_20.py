import mmap
import os
import re
import sys
import time
from collections import defaultdict
from datetime import datetime
from itertools import chain
from operator import itemgetter
from typing import Dict, List, Optional, Set, Tuple, Union

from colorama import Fore, Style
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import get_lexer_by_name
from pygments.lexers.special import TextLexer
from pygments.util import ClassNotFound
from tabulate import tabulate

from . import __version__
from .config import Config
from .constants import (
    DEFAULT_CONFIG_PATH,
    DEFAULT_CONFIG_PATH_OLD,
    DEFAULT_EXCLUDE_PATHS,
    DEFAULT_EXCLUDE_PATTERNS,
    DEFAULT_EXCLUDE_PATTERNS_OLD,
    DEFAULT_EXCLUDE_PATTERNS_VCS
