import ctypes
import ctypes.util
import threading
import sqlite3
from time import time, sleep
from collections import defaultdict
from pycparser import c_parser, c_ast, parse_file

from .utils import *


class _KernelEvent(object):
    __slots__ = ('name', 'time', 'args', 'trace', 'trace_len')

    def __init__(self, name, time=None, args=None, trace=None, trace_len=0):
        self.name = name
        self.time = time
        self.args = args
        self.trace = trace
        self.trace_len = trace_len

    def __str__(self):
        return '%s(%s)' % (self.name, ', '.join('%s=%s' % (k, v) for k, v in self.args.iteritems()))


class Event(object):
    def __init__(self, name, extra_args={}):
        self.name = name
        self.extra_args = extra_args

    def __call__(self, f):
        @wraps(f)

