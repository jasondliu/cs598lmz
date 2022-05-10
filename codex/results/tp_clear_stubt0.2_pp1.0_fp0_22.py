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

# This is a bit tricky.  The LateFin object is not yet collected, because
# it has a reference to the function object.  The function object is not
# yet collected, because it has a reference to the module object.  The
# module object is not yet collected, because it has a reference to the
# tuple object.  The tuple object is not yet collected, because it has a
# reference to the LateFin object.  The LateFin object is not yet collected,
# because it has a reference to the function object.  The function object is
# not yet collected, because it has a reference to the module object.  The
# module object is not yet collected, because it has a reference to the
# tuple object.  The tuple object is not yet collected, because it has a
# reference to the LateFin object.  The LateFin object is not yet collected,
# because it has a reference to the function object.  The function object is
# not yet collected, because it has a reference to the module object.  The
# module object is not yet collected, because it has a reference to the
#
