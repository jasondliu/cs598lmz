import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return range(10)

def f():
    fun()

f()
</code>
Then I'm getting a strange segfault.
It's not reproducible with <code>numba.jit(nopython=True)</code> for example.
Any idea about this?
EDIT: the crash is pretty reproducible with the latest LLVM 4.0, but not with the previous version 3.9.1. 


A:

This is a known bug in LLVM 4.0. It should be fixed in the next release.

