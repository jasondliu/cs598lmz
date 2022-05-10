fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #10887
import os
import sys

class A(object):
    def __init__(self):
        self.f = open('/dev/null', 'w')
    def __del__(self):
        self.f.close()

def f():
    a = A()
    os.write(a.f.fileno(), b'x')

f()
gc.collect()

# Issue #11486
def f():
    def g():
        pass
    g.__code__ = None
    g()
f()

# Issue #12079
import warnings

def f():
    def g():
        pass
    g.__code__ = None
    warnings.warn("foo", RuntimeWarning, stacklevel=2)

f()

# Issue #12091
def f():
    def g():
        pass
    g.__code__ = None
    raise RuntimeError()

try:
    f()
except RuntimeError:
    pass

# Issue #12092
def f():
