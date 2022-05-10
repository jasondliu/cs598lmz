import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc

# This is a little tricky.  The __del__ method of the Cyclic class
# is the last thing called.  It sets the ref attribute of the
# latefin instance to a weak reference to its first argument.  The
# first argument is the func object, which has its __module__
# attribute set to the cyc object.  So in order to break the cyclic
# reference, we need to delete the cyc object.  But we can't do that
# from this __del__ method, because that would leave the weakref
# object (with a callback pointing to the __del__ method) alive.  So
# instead, we set func to the weakref itself, and arrange for the
# weakref to delete itself when it gets called.

# Here's a traceback showing what's happening:
#
# Traceback (most recent call last):
#   File "./python", line 29, in <module>
#   File "./python", line 25, in __del__
# ReferenceError: weakly-referenced object no longer exists
# Exception AttributeError: "'NoneType' object has no
