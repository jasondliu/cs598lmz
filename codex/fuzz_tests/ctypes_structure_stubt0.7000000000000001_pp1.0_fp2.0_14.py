import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def foo():
    return ctypes.sizeof(S)

print(foo())
</code>
With ctypes, the size of an instance of S is 4, but with cppyy, it is 8.
This seems to be related to cppyy mis-recognizing <code>c_int</code> as an <code>int</code> instead of an <code>int*</code>.
Is there any way to work around this?

