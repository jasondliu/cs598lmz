import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
def go():
    fun()
go()
</code>
But if I try to compile the file with <code>cythonx</code> it gets stuck at <code>go()</code>. (It doesn't hang, it just doesn't do anything.) As far as I can tell, this is a bug in the current version (0.21).
I'm interested in using Cython for wrapping C++ classes, and I'm very happy I don't have to write out the signatures for all the methods by hand.
For now, I'll just use the Cythonx-generated <code>.pxd</code> file, until the bug is fixed.

