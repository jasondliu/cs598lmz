import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import sys
import os
import time
import shutil
import tempfile
import unittest
from test import test_support
from test.test_support import TESTFN, unlink

# Skip test if _sqlite3 was not built or the extension module is in use.
test_support.import_module('_sqlite3')

try:
    from collections import namedtuple
except ImportError:
    # Python < 2.6
    def namedtuple(typename, field_names):
        def new(**kw):
            return tuple.__new__(nt, (kw[n] for n in field_names))
        nt = type(typename, (tuple,), {'__new__': new,
                                        '__repr__': lambda self:
                                            '%s(%s)' % (typename,
                                                        ', '.join('%s=%r' % e
                                                                  for e in zip(field_names, self))),
                                        '__slots__': ()})
        return nt
