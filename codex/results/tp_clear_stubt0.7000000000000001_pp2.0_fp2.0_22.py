import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc

latefin.ref = weakref.ref(func)
del latefin

gc.collect()
gc.collect()
gc.collect()

if func is not None:
    print "FAIL"
    raise SystemExit
else:
    print "OK"
"""

test_gc_concurrent_finalizers_2 = """
import sys, gc
def foo():
    print >>sys.stderr, "finalizing foo"

class C(object):
    def __del__(self):
        print >>sys.stderr, "finalizing C"
        foo()

gc.disable()

c = C()

gc.collect()
gc.collect()

gc.enable()

gc.collect()
gc.collect()

print "OK"
"""

test_traceback_print = """
import sys
import traceback

try:
    raise ValueError('spam', 'eggs')
except ValueError:
    tb = sys.exc_info()[2]
    traceback.print_tb(tb)
