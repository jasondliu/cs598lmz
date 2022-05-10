import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
f=weakref.finalize(a,callback,[lst])
f.atexit=False
del a
fn=finalize._detect_reference_cycles()
if fn is None:
    fn,l=finalize._find_cycle()
keepalive.append(l)
keepalive.append(fn)


import unittest
from test import support

from weakref import ref, proxy, finalize, ref_type


class X(object):
    pass

class FinalizeTest(unittest.TestCase):

    def callback(*args): pass

    def test_finalize_noargs(self):
        x = X()
        f = finalize(x, FinalizeTest.callback)
        self.assertEqual(f.alive, True)
        del x
        support.gc_collect()
        self.assertEqual(f.alive, True)
        FinalizeTest.callback = self.callback = lambda: setattr(f, 'called', 1)
        support.gc_collect()
        self.assertEqual(getattr(f
