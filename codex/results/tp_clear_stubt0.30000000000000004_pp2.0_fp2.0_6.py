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

# This is a hack to make sure that the above code is not optimized away.
# The test is meaningless if the above code is optimized away.
# The test is also meaningless if the above code is not executed.
# The test is meaningless if the above code is executed more than once.
# The test is meaningless if the above code is executed before the
#   interpreter is fully initialized.
# The test is meaningless if the above code is executed after the
#   interpreter is finalized.
# The test is meaningless if the above code is executed before the
#   garbage collector is fully initialized.
# The test is meaningless if the above code is executed after the
#   garbage collector is finalized.
# The test is meaningless if the above code is executed before the
#   weakref module is fully initialized.
# The test is meaningless if the above code is executed after the
#   weakref module is finalized.
# The test is meaningless if the above code is executed before the
#   weakref module is fully initialized.
# The test is meaningless if the above code is executed after the
#   weakref module is finalized.
#
