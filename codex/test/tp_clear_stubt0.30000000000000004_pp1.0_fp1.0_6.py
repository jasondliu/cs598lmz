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

# This should not crash, but it does.  The problem is that the
# LateFin.__del__() method is called, and it tries to access the
# 'ref' attribute of the second element of the tuple.  But the
# tuple is already dead, and so the 'ref' attribute is not found.
# The problem is that the tuple is not dead, it is just unreachable
# from the root.  The tuple is still alive because the LateFin
# object is still alive.  The LateFin object is still alive because
# it is in the tuple.  The tuple is still alive because the LateFin
# object is still alive.  The LateFin object is still alive because
# it is in the tuple.  The tuple is still alive because the LateFin
# object is still alive.  The LateFin object is still alive because
# it is in the tuple.  The tuple is still alive because the LateFin
# object is still alive.  The LateFin object is still alive because
# it is in the tuple.  The tuple is still alive because the LateFin
# object is still alive. 
