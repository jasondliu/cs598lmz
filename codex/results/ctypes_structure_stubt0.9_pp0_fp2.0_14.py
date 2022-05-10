import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int.in_dll(ctypes.CDLL("__PYFEYMINIMAL_MODULE__"), "x").value
    def __repr__(self):
        return "S(%s)" % (S.x,)

S.x += 10

def f(x):
    return x + x

_f_thunks = [f]
