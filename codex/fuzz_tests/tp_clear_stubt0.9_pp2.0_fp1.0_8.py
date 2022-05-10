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
del func, cyc, latefin
gc.collect()
</code>
which crashes with this stack trace (on a 64-bit machine):
<code>*** glibc detected *** /home/users/david/.virtualenvs/Py3/bin/python: double
free or corruption (!prev): 0x080e0e30 ***
======= Backtrace: =========
/lib/libc.so.6(+0x75ee3)[0xb7417ee3]
/lib/libc.so.6(cfree+0x6d)[0xb741da9d]
/usr/lib/python3.1/lib-dynload/_hashlib.so(+0x230f)[0xb7e380f]
/usr/lib/python3.1/lib-dynload/_hashlib.so(+0x231e)[0xb7e381e]
/usr/lib/python3.1/lib-dynload/_hashlib.so(+0x23dd)[0xb7e38dd]
/usr/lib/python3.1/lib-dynload/_
