import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong(10)

def func(arg):
    return arg.x

lib = ctypes.CDLL(None)
print ctypes.sizeof(S)
lib.test.argtypes = [ctypes.POINTER(S)]
lib.test.restype = ctypes.c_longlong

s = S()
print lib.test(s)
print lib.test(ctypes.byref(s))
print lib.test(ctypes.pointer(s))
print lib.test(ctypes.pointer(s))
s2 = S()
s2.x = 3
print lib.test(s2)
s3 = S()
s3.x = 7
print lib.test(s3)

print func(s3)
print func(ctypes.pointer(s3))
</code>
Note: I copied in your code and changed the <code>S</code> structure to have a <code>c_longlong</code> field.  Now the size of <code>S</code> is 8 bytes which matches the size of <code
