import weakref
# Test weakref.ref() with a function.
import gc
import sys
import weakref

def f():
    pass

def callback(r):
    print 'callback called'
    raise Exception

def test():
    r = weakref.ref(f, callback)
    print 'callback set'
    del f
    print 'f deleted'
    gc.collect()
    print 'gc done'

test()
