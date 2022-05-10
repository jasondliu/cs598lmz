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

# The following line will crash the Python interpreter, because the
# __del__ method of 'cyc' is called, and the __del__ method of
# 'latefin' is called, and the __del__ method of 'func' is called.
# The __del__ method of 'func' is called, because 'func' is a
# local variable in the __del__ method of 'cyc'.  It is a local
# variable in the __del__ method of 'cyc', because the __del__
# method of 'cyc' is called, because 'cyc' is a local variable in
# the __del__ method of 'func'.
#
# The interpreter is not able to detect the cyclic reference,
# because 'func' is a local variable in the __del__ method of
# 'cyc'.  The interpreter is not able to detect the cyclic
# reference, because 'cyc' is a local variable in the __del__
# method of 'func'.
#
# The interpreter will crash, because the __del__ method of 'func'
# is called, and the
