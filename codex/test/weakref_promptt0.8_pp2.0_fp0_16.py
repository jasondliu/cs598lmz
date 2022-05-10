import weakref
# Test weakref.ref() on a slice
class X:
    pass

x = X()
r = weakref.ref(x.__doc__)
r.__init__(x.__doc__)
r
r()
r.__init__(x)
r
r()
del x
