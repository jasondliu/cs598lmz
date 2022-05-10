import mmap
import os
import re
import sys
import time
import traceback

from collections import defaultdict
from datetime import datetime
from functools import partial
from itertools import chain
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from os import path
from subprocess import Popen, PIPE
from tempfile import NamedTemporaryFile
from threading import Thread

from . import __version__
from . import config
from . import constants
from . import errors
from . import log
from . import utils
from . import vcs
from .compat import (
    FileNotFoundError,
    PermissionError,
    ProcessLookupError,
    TemporaryDirectory,
    WindowsError,
    is_win32,
    is_win64,
    open,
    path_to_bytes,
    path_to_unicode,
    subprocess_check_output,
    subprocess_check_output_error_ok,
    subprocess_check_output_error_ok_win,
    subprocess_check_output_
