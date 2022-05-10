import weakref
# Test weakref.ref constructor
import support

class C:
    pass

def key(ref):
    return ref()

def test(object):
    r = weakref.ref(object, key)
    r()
    return r

def test2(object):
    r = weakref.ref(object, key)
    r2 = weakref.ref(object, key)
    r()
    r2()
    return r

def test3(object):
    r = weakref.ref(object, key)
    r2 = weakref.ref(object, key)
    r()
    del r
    r2()
    del r2
    return object

def test4(object):
    r = weakref.ref(object, key)
    r2 = weakref.ref(object, key)
    del r2
    r()
    del r
    return object

def test5(object):
    r = weakref.ref(object, key)
    r2 = weakref.ref(object, key)
    del r2
    r()
   
