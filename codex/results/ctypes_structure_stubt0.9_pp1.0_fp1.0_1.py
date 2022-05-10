import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p.in_dll(ctypes.pythonapi, "PyFile_Type")
</code>
This is meaningless, but it does compile.

