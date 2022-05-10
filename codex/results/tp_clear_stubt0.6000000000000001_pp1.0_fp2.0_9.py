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
del latefin
gc.collect()

# Fails with:
# Fatal Python error: deallocating None
#
# See also: http://bugs.python.org/issue1182542
#
# The problem is that when func is finalized, the __dict__ is not
# yet finalized, so the __dict__ is still present in the cyclic
# garbage.
#
# When the __dict__ is finalized, it tries to remove the __module__
# key, which is not present anymore, so it calls the next_in_mro
# slot of the type of the __dict__, which is a methodwrapper.
#
# The methodwrapper calls PyObject_Call, which tries to call
# the __call__ slot of the PyMethodDescrObject.
#
# The PyMethodDescrObject is part of the latefin object, so
# it is freed.
#
# The PyMethodDescrObject has a PyDescr_COMMON struct as part
# of it, which has a d_common.d_type slot.
#
# The d_type slot is a
