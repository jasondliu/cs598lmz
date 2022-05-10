import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float.in_dll(ctypes.pythonapi, "x")
    y = ctypes.c_float.in_dll(ctypes.pythonapi, "y")
    z = ctypes.c_float.in_dll(ctypes.pythonapi, "z")
</code>
In this case, <code>S</code> is a structure with three float members, <code>x</code>, <code>y</code> and <code>z</code>.  These members are initialized from the values in the global variables <code>x</code>, <code>y</code>, and <code>z</code> in the Python C API.

