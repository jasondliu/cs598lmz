import weakref
# Test weakref.ref() and weakref.proxy()

import weakref
import gc

class Foo:
    pass

def callback(r):
    print('called back with', r)

def test():
    f = Foo()
    r = weakref.ref(f, callback)
    p = weakref.proxy(f, callback)
    print('initial state:', r(), p.__dict__)
    f.x = 42
    print('after f.x = 42:', r(), p.__dict__)
    del f
    gc.collect()
    print('after deleting f:', r(), p.__dict__)

test()
