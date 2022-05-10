import weakref
# Test weakref.ref that points to an object with a finalizer.
import gc

class Foo:
    def __del__(self):
        pass

def bar():
    pass

alive = []
def foo(x):
    alive.append(2)
    del alive[:]

def callback(x):
    for i in range(100000):
        r = weakref.ref(Foo(), callback)
        del r
        x.bar()

R = weakref.ref(Foo(), foo)
R()
del R
del Foo
for i in range(1000):
    r = weakref.ref(Foo(), foo)
    del r
R = weakref.ref(Foo(), callback)
gc.collect()
