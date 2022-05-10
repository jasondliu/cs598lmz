import weakref
# Test weakref.ref() in a function.
def f():
    l = [1, 2, 3]
    r = weakref.ref(l)
    return r

