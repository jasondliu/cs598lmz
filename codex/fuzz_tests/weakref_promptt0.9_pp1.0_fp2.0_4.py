import weakref
# Test weakref.ref versus _weakkeydict

class X(object):
    pass

class Y:
    pass

def f(x):
    x.foo = 42
    return weakref.ref(x)

def g(x):
    x.foo = 42
    return _weakref.ref(x)

if __name__=='__main__':
    for type, ref in ((X, f), (Y, g)):
        x = type()
        r = ref(x)
        assert r() is x
        assert r().foo == 42
