import weakref
# Test weakref.ref for builtin and extension types.

# (Based on test_weakref.py, which is more thorough on the builtin
# types, but skips the extension types.)

import gc
import sys
import unittest
import weakref
import weakrefset

from test import support

class Foo:
    pass

class Foo2:
    def __init__(self):
        self.wr = weakref.ref(self)

class Foo3(Foo):

    def __init__(self):
        self.wr = weakref.ref(self)

class Foo4(Foo3):
    pass

class Foo5:
    pass

def bar(x):
    pass

def make_test(x):
    return lambda: bar(x)

def bar2(x):
    return x

def make_test2(x):
    return lambda: bar2(x)

@unittest.skipUnless(sys.version_info < (3,), 'Only relevant for Python 2')
class TestWeakrefs(unittest.Test
