import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int.in_dll(ctypes.pythonapi, "x")

print S.x
</code>
This prints <code>c_int(0)</code> as expected.

