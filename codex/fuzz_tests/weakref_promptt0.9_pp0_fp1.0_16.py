import weakref
# Test weakref.ref(p) and weakref.proxy(p) after removing ref to p
# XXX Seems like CPython's weakref.c isn't clever enough when there
#     is only one reference to an object!  (In particular it doesn't
#     immediately decay the weakref to dead state.)  At least, I'm
#     seeing this failure on some machines...
import gc
class BaseTest(unittest.TestCase):
    def test(self):
        p = self.Proxy(42)
        r = weakref.ref(p)
        self.assertEqual(r(), p)
        self.assertEqual(r(), 42)
class TestRef(BaseTest):
    Proxy = staticmethod(weakref.ref)
class TestProxy(BaseTest):
    Proxy = staticmethod(weakref.proxy)
class ReprProxy:
    def __init__(self, proxied_object):
        object.__setattr__(self, '_subject', proxied_object)
        object.__setattr__(self, '_message',
          'the proxy of ' + repr(prox
