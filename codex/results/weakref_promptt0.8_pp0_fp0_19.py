import weakref
# Test weakref.ref() and weakref.proxy()
import copy
import pickle
import gc
import sys
import unittest
from test.support import run_unittest, import_module
from collections import OrderedDict
try:
    import _testcapi
except ImportError:
    _testcapi = None

# To avoid triggering the cyclic garbage collector
if hasattr(sys, "getcheckinterval"):
    sys.setcheckinterval(100*100)

#
# Test the basic operation.
#

class C:
    pass

class R:
    pass

class C_newstyle(object):
    pass

class R_newstyle(object):
    pass

class D(R_newstyle):
    pass

class E(D):
    pass

class F(C):
    pass

class G(E, C):
    pass

class Z(D, F):
    pass

class F_newstyle(C_newstyle):
    pass

class G_newstyle(E, C_newstyle):
    pass
