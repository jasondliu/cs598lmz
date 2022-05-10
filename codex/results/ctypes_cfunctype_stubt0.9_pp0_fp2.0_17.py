import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'yeah'

fun.restype = int
print(fun())
</code>
this also gives a segfault. Is there a work around for this?


A:

This is a known bug in PyPy, which has been fixed in their latest release. I've confirmed that it no longer segfaults on CPython 2.7.13 and PyPy 5.8.
Answer from the PyPy bug tracker.

