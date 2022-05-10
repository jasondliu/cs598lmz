import weakref
# Test weakref.ref(callable)

def f():
    pass

def g():
    pass

class X:
    def __call__(self):
        pass

class Y:
    def __get__(self, obj, objtype):
        pass

class Z:
    def __init__(self, *args, **kw):
        pass

for o in f, g, X(), Y(), Z:
    try:
        r = weakref.ref(o)
    except TypeError:
        pass
    else:
        r()
