import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import sys
import os
import re
import logging
import subprocess
import tempfile
import json
import inspect
import platform
import traceback
import errno
import signal
import math
import collections

from . import __version__
from . import config
from . import util
from . import log
from . import vpn
from . import dns
from . import block
from . import tld
from . import pihole
from . import watch
from . import filter
from . import report
from . import stats
from . import sqlite
from . import dnssec

from .util import *

_libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
_libc.prctl.argtypes = [ctypes.c_int, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong]
_libc.prctl.restype = ctypes.c_int

PR_SET_NAME = 15
PR
