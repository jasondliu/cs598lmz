import weakref
# Test weakref.ref()
import sys
import os

class C(object):
    pass

c = C()
r = weakref.ref(c)
