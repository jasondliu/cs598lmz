import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs.
import _weakref

class Foo(object):

    def __del__(self):
        self.foo = 1

def fPreserve(x):
    global obj
    if obj is None:
        return
    x.foo = obj.foo

gc.enable()

f = Foo()
obj = f

wf = weakref.ref(f, fPreserve)

dels = []
def fDel(x):
    dels.append(1)

wd = weakref.ref(f, fDel)

del f

gc.collect()

print len(dels)
if dels:
    raise RuntimeError

print obj.foo

gc.collect()

print obj
if obj is not None:
    raise RuntimeError

print wd()
if wd() is not None:
    raise RuntimeError

print wf()
if wf() is not None:
    raise RuntimeError

# And again, in case it makes a difference.

f = Foo()
obj = f


