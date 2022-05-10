import weakref
# Test weakref.ref() on a function
class C:
    pass
def f(): pass
r = weakref.ref(f)
r()
r = weakref.ref(C)
r().a = 1
del r()
del r
# This is a different test.  Function objects are not
# supposed to be weakly referencable.
try:
    import weakref
    r = weakref.ref(C)
except TypeError:
    pass
else:
    print "weakref.ref(function) should raise TypeError"

# Test weakref callbacks on a function
def cb(*args):
    print "callback called with", args
def f(a):
    print "f() called with", a
    return a
w = weakref.ref(f, cb)
x = w()
cb.called = 0
del x
if not cb.called:
    print "del x didn't call the callback"

# Test weakref callbacks on a class
class C:
    def __init__(self, a):
        self.a = a
    def __del__
