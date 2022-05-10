import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')
import os
import time
import sys
import traceback

# Python 3 compatibility
try:
    import Queue as queue
except ImportError:
    import queue

try:
    import unittest2 as unittest
except ImportError:
    import unittest

try:
    from unittest import mock
except ImportError:
    import mock

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO

try:
    from itertools import izip
except ImportError:
    izip = zip

try:
    from itertools import imap
except ImportError:
    imap = map

try:
    from itertools import filterfalse
except ImportError:
    filterfalse = itertools.ifilterfalse
