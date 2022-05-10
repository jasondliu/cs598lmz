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

import gc
gc.collect() # Reference finalizer object
gc.collect()
import gc
gc.collect()
res = ref()
fail(res is not None, "atexit handler lost")

##def check():
##  a = None
##  def handler():
##    fail('atexit.handler', a is not None)
##  try:
##    import atexit
##    atexit.register(handler)
##    a = 1
##    del atexit
##  except Exception:
##    pass
##  else:
##    try:
##      del a # some Python implementations don't raise SystemExit when
##            # exceptions are occurring in atexit handlers
##    except Exception:
##      pass
##
##stuff.append(check)

def test_generator1():
    def simple():
        yield 42
        yield 24
    g = simple()
    assert g.next() == 42
    assert g.next() == 24
