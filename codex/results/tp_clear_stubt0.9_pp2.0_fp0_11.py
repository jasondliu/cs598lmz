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
del func, cyc, LateFin, Cyclic
gc.collect()

import asyncore, types
m = asyncore.dispatcher(0)
m.handle_connect = 0
m.handle_accept = 0
m.handle_expt = 0
m.handle_read = 0
m.handle_write = 0
f = lambda: m
m.handle_close = f
m.handle_error = f
a = types.FunctionType(type(repr).__code__, {}, '_str', argdefs=(), closure=())

m.accept = a
m.close = a
m.connect = a
m.recv = a
m.send = a
m.del_channel = a

del a, f, m, asyncore, types
gc.collect()
