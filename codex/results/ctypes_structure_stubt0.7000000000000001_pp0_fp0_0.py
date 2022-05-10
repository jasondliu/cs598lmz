import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def f(x):
    if x:
        raise ctypes.ArgumentError

class X(ctypes.Structure):
    _fields_ = [("p", ctypes.POINTER(S)), ("f", ctypes.CFUNCTYPE(None, ctypes.POINTER(S)))]

def main():
    x = X()
    x.p = ctypes.pointer(S())
    x.f = ctypes.CFUNCTYPE(None, ctypes.POINTER(S))(f)
    x.f(x.p)

main()
