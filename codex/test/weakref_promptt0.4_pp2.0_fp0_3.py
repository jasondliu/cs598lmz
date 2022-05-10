import weakref
# Test weakref.ref(object)

def f(x):
    return weakref.ref(x)

class C:
    pass

c = C()
r = f(c)
