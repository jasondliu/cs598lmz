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

# The following line will crash the interpreter:
del latefin
</code>
This is the crash report:
<code>Program received signal SIGSEGV, Segmentation fault.
0x00007ffff7a6a7d0 in PyObject_Call () from /usr/lib/libpython3.4m.so.1.0
(gdb) bt
#0  0x00007ffff7a6a7d0 in PyObject_Call () from /usr/lib/libpython3.4m.so.1.0
#1  0x00007ffff7a6a8c8 in PyEval_EvalFrameEx () from /usr/lib/libpython3.4m.so.1.0
#2  0x00007ffff7a6d7d8 in PyEval_EvalCodeEx () from /usr/lib/libpython3.4m.so.1.0
#3  0x00007ffff7a6d8a4 in PyEval_EvalCode () from /usr/lib/libpython3.4m.so.
