import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

S.x.__doc__ = "this is the docstring"

# test the docstring
assert S.x.__doc__ == "this is the docstring"

# test the docstring with the new API
