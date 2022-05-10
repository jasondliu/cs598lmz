import weakref
# Test weakref.ref
try:
    import _weakref
    _weakref.getweakrefcount
except ImportError:
    import _weakref
    _weakref.getweakrefcount = lambda x: len(x.data)

import unittest
from test import test_support

class Foo:
    pass

class Foo2:
    pass

class Foo3:
    pass

class Foo4:
    pass

class Foo5:
    pass

class Foo6:
    pass

class Foo7:
    pass

class Foo8:
    pass

class Foo9:
    pass


class Callback:
    def __init__(self):
        self.called = 0
        self.last_obj = None

    def __call__(self, ref):
        self.called += 1
        self.last_obj = ref()


class MyBase:
    def __init__(self, callback=None):
        self.callback = callback

    def __del__(self):
        if self.callback:
            self.callback(self)

class
