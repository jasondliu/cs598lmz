import weakref
# Test weakref.ref()
# Create some objects to be used as keys in the dictionary

ns1 = {1:'one', 2:'two'}
ns2 = {'a':'A', 'b':'B'}

class C: pass

c1, c2 = C(), C()

def f(): pass

def showref(ref):
    print('deleted:' if ref() is None else 'not deleted:', ref)

def trickyfunc(o):
    showref(o)
    return "Tricky!"

def test_ref():
    # Test weak references
    rf = weakref.ref(ns1)
    showref(rf)
    ns2 = ns1
    showref(rf)
    del ns1
    showref(rf)
    ns1 = rf()
    print("ns1:", ns1)

    print("*** Reference to a function ***")
    rf = weakref.ref(f)
    showref(rf)
    del f
    showref(rf)
    print("function:", rf())

    print("***
