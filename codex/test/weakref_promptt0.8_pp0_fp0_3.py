import weakref
# Test weakref.ref() and weakref.proxy() on all types
import bz2
import operator
import os
import select
import sys
import threading
import time
import tokenize
import traceback
import types
import unittest
import zipfile

from test import mapping_tests
from test import test_support

class C:
    pass

class D:
    pass

class SelfRef:
    def __init__(self):
        self.self = self

# Try to cause a segfault.  We don't care if it succeeds, or even if it
# makes any sense.  A sys.stderr traceback can't hurt, though.
def kill_referent(r):
    r()
    time.sleep(0.01)

######################################################################
# Basic tests

