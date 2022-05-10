import io
# Test io.RawIOBase
import keyword
import locale
import math
import operator
import os
import pickle
# Test pickle.Pickler
import platform
import re
import reprlib
import select
# Test select.epoll
# Test select.kqueue
import shlex
import shutil
import signal
import socket
# Test socket.socket
import stat
import struct
# Test struct.Struct
import sys
import threading
import time
import traceback
import unittest
import unicodedata
import uuid
import weakref

import datetime
# Test datetime.datetime
import contextlib
import functools
import itertools
import os.path
import queue
import subprocess
import test.support

# Test sys.implementation
# Test sys.api_version

import xml.etree.ElementTree

try:
    import _testcapi
except ImportError:
    pass

class ABCTest(unittest.TestCase):
    def test_ABC(self):
        self.assertTrue(issubclass(dict, dict))
        self.assertTrue(issubclass(
