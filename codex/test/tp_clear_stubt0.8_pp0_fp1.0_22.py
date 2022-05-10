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

# import _weakref, gc
#
# class X(object):
#     pass
#
# x = X()
# ref = _weakref.ref(x)
#
# class M(object):
#     def __del__(self):
#         print 'a'
#         print ref()
#
# m = M()
# m.__module__ = x
#
# del x, ref, m
# gc.collect()
