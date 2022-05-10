import weakref
# Test weakref.ref(Class.method) support
from weakref import ref as weakref_ref
from weakref import proxy as weakref_proxy

import _testcapi

from test import support

# A mixin class for testing weakrefs on objects with custom __hash__ or __cmp__
class Hashed:
    def __init__(self, arg):
        self.arg = arg
        self.hashcount = 0

    def __hash__(self):
        self.hashcount += 1
        return hash(self.arg)

    def __eq__(self, other):
        return self.arg == other

    def __ne__(self, other):
        return not self == other

class Cmped(Hashed):
    def __cmp__(self, other):
        return cmp(self.arg, other)

# Test weakref.ref(object) and weakref.proxy(object)
class TestBasic(unittest.TestCase):

    def setUp(self):
        self.spam = []
        self.wref = weakref.ref(self.spam)
