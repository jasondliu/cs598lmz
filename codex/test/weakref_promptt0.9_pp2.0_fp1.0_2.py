import weakref
# Test weakref.ref()
import glob
import os
import errno
import stat
import time
try:
    any
except NameError:
    from future_builtins import any
fnr = weakref.ref
del weakref

import unittest
from test import test_support

class X(object):
    pass

class Y(X):
    pass

def sub(l, i):
    l.append(i)

class Wrs:

    def check(self, a, b):
        if a is b:
            return None
        return '%r should be %r' % (b, a)

    def test_callback(self):
        x = X()
        x.b = X()
        wr = fnr(x, sub, [x])
        del x
        c, i = wr.wr_called
        self.assert_(c is sub)
        self.assert_(i is wr.key())
        x = i
        self.assertEqual(wr.wr_result, [x])
