import ctypes
ctypes.cast(pointer, type)
</code>
But I don't know how to use it in my code.
I'm using Python 2.4 and 2.7 with ctypes and pywin32.
EDIT:
I've tried to use ctypes:
<code>    self.lib.set_fundamentals.restype=ctypes.POINTER(ctypes.c_double)
    arr = self.lib.set_fundamentals(ctypes.c_int(len(fundamentals)), ctypes.c_double(fundamentals[0]))
</code>
but now I'm getting the error: 
<code>ValueError: Procedure probably called with not enough arguments (4 bytes missing)
</code>
EDIT2:
In the end I've solved the problem by using numpy.ctypeslib.

