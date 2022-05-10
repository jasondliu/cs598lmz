import gc, weakref
import sys

class Dummy:
    pass

def callback(ref):
    print 'callback(', ref, ')'

def test():
    d = Dummy()
    print 'd =', d
    r = weakref.ref(d, callback)
    print 'r =', r
    print 'd =', d
    print 'r() =', r()
    print 'deleting d'
    del d
    gc.collect()
    print 'r() =', r()

test()
