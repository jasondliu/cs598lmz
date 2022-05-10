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
gc.collect()
gc.collect()
</code>
<code>$ python -u crash.py

Program received signal SIGSEGV, Segmentation fault.
0x00000000027a1cb6 in PyObject_CallObject () from /usr/lib/python2.7/lib-dynload/_gc.so
(gdb) bt
#0  0x00000000027a1cb6 in PyObject_CallObject () from /usr/lib/python2.7/lib-dynload/_gc.so
#1  0x00000000027a1f3c in collect () from /usr/lib/python2.7/lib-dynload/_gc.so
#2  0x00000000027a20ac in collect () from /usr/lib/python2.7/lib-dynload/_gc.so
#3  0x00000000027a20ac in collect () from /usr/lib/python2.7/lib-dynload/_gc.so
#4  0x0000000000438c42 in PyEval_Eval
