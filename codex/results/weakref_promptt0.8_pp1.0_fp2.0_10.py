import weakref
# Test weakref.ref, weakref.proxy, and weakref.CallableProxyType

from test import test_support
from test.test_support import import_module

warnings = import_module('warnings')

# Issue 2317: weakref.ref(Exception) crash
class MyException(Exception):
    pass
def f():
    weakref.ref(MyException)


class TestWeakref:

    def callback(self, object):
        self.__class__.called = 1

    def test_basic(self):
        called = []
        class Foo(object):
            def __init__(self):
                self.__class__.nselfs = nselfs = self.__class__.nselfs + 1
            def __del__(self):
                self.__class__.ndels = ndels = self.__class__.ndels + 1
                called.append(None)
        Foo.nselfs = Foo.ndels = 0
        f1 = f2 = f3 = f4 = None
        f1 = Foo()
        wp = weakref.proxy
