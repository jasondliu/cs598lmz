import ctypes

class S(ctypes.Structure):
    x = ctypes.CFUNCTYPE(ctypes.POINTER(S))

s = S()
s.x = s.x(s)
</code>
This will recurse until the stack overflows, just like the equivalent Python code.

