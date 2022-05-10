import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
f=weakref.ref(lst,callback)
lst = None

try:
    import threading
except ImportError:
    import dummy_threading as threading
import weakref
import unittest

class BaseTestCase(unittest.TestCase):

    def callback(self, x):
        self.callback_called = True
        self.callback_arg = x

    def setUp(self):
        self.callback_called = False
        self.callback_arg = None

    def tearDown(self):
        for r in self.keepalive:
            del r

    def testBasic(self):
        # This is a basic sanity check.  It doesn't verify that the
        # callback got called.
        self.keepalive = [str()]
        f = weakref.ref(self.keepalive[0], self.callback)
        keepalive = self.keepalive
        del self.keepalive
        del keepalive[0]

    def assertCallback(self, arg
