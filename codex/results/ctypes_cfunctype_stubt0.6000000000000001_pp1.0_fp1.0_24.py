import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 3

for i in range(100000):
    fun()
</code>
The memory footprint increases by ~1.5MB every time the function is invoked.
I tried to gc.collect() but it has no effect.
How can I avoid this memory leak?


A:

This is a CPython implementation detail, not a bug.
When a function is called, a reference to its globals is stored in the frame object. When the function returns, the reference is released.
Unfortunately, the reference is stored in a dictionary in the frame object. The dictionary grows as more references are added.
The memory is reclaimed when the frame object is destroyed, but the dictionary is never shrunk.
This is the same reason that global variables leak memory in CPython.

