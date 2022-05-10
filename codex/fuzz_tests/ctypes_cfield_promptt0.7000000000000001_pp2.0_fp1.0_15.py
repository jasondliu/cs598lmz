import ctypes
# Test ctypes.CField instance
import datetime
import decimal
import functools
import mmap
# Test ctypes.PyCSimpleType instance
import os
import operator
import pickle
import pprint
import re
import signal
import sys
import time
import unittest
import unicodedata
import zlib
import builtins

from test import mapping_tests
from test import support
from test import test_grammar
from test import test_opcodes

try:
    import threading, _thread
except ImportError:
    threading = _thread = None

import io
import weakref
import contextlib

# Test asynchat.async_chat
import asynchat

# Test binhex
import binhex

# Test bz2
import bz2

# Test cgi.test
import cgi

# Test cookielib
import cookielib

# Test cPickle
import cPickle

import distutils.sysconfig

# Test email package
import email

# Test fcntl
try:
    import fcntl
except ImportError:

