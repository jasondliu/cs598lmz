import weakref
# Test weakref.ref()

import weakref

class C(object):
    pass

c = C()

def test():
    r1 = weakref.ref(c)
    r2 = weakref.ref(c)
    try:
        r1() # dereference r1
    except NameError:
        return
    assert 0, 'NameError not raised'

try:
    test()
except NameError:
    pass
else:
    assert 0, 'NameError not raised'

# Test weakref callbacks

def test(data, callback):
    ref = weakref.ref(data, callback)
    if ref:
        ref()

def test_callback(ref):
    raise NameError

def test_ref(data):
    return weakref.ref(data, test_callback)

def do_nothing(ref):
    pass

def do_nothing_ref(data):
    return weakref.ref(data, do_nothing)

class GcError(Exception):
    pass

class A:
    pass

def raise_error_
