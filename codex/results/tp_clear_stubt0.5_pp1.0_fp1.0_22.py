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
gc.collect()

# The above code creates a cyclic structure, with a function and a tuple
# element both referring to the tuple.  The tuple has a __del__() method
# that creates a weak reference to the function.  The function has a
# __module__ attribute that refers to the tuple.  The tuple element has
# a __slot__ attribute.
#
# When the cyclic trash is collected, the __del__() method is run.  This
# creates a weak reference to the function.  The function is not yet
# dead, so the weak reference callback has not yet been invoked.  The
# weak reference is stored in a global variable.  The __del__() method
# then deletes the global variable 'latefin', which is the last reference
# to the tuple element.  The tuple element is not yet dead, because the
# function is still alive.  The tuple element has a __slot__ attribute,
# so it is resurrected.  This resurrects the function, too.  The function
# is now dead again, so the weak reference callback is invoked, setting
# the global variable 'func' to
