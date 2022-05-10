import ctypes
# Test ctypes.CFUNCTYPE
# This is not very sensitive to the actual types;
# it just makes sure that the right number of arguments are passed
# and the right number of values are returned.
def test():
    lib = ctypes.CDLL(ctypes.util.find_library("m"))
    FunctionType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
    c_sin = FunctionType(("sin", lib), ((1, "x"),))
    c_cos = FunctionType(("cos", lib), ((1, "x"),))
    c_pow = FunctionType(("pow", lib), ((1, "x"), (1, "y")))
    for i in range(1, 5):
        for j in range(1, 5):
            if abs(c_sin(i) - math.sin(i)) > 0.0001:
                raise RuntimeError("sin(%d) = %f, should be %f" % (
                    i, c_sin(i), math.sin(i)))
