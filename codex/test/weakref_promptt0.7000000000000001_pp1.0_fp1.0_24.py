import weakref
# Test weakref.ref() with a hashable class

from test import support

class C:
    pass

def callback(r):
    print('callback(%r)' % r)

def test(verbose=0):
    if verbose:
        print("Testing weakref.ref() with hashable class...")
    obj = C()
    obj.attr = 1
    r = weakref.ref(obj, callback)
    if verbose:
        print("  obj:", obj)
        print("  ref:", r)
        print("  referent:", r())
    obj2 = r()
    if verbose:
        print("  obj2:", obj2)
        print("  obj is obj2:", obj is obj2)
        print("  obj == obj2:", obj == obj2)
    obj3 = weakref.proxy(obj)
    if verbose:
        print("  obj3:", obj3)
        print("  obj is obj3:", obj is obj3)
        print("  obj == obj3:", obj == obj3)
       
