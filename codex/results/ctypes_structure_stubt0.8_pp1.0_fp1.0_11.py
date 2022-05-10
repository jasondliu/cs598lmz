import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_float

def test1():
    s = S(5, 0.5)
    pywintypes.PYFUNCTYPE(ctypes.c_int, ctypes.POINTER(S))(lambda n: n)

def test2():
    pywintypes.PYFUNCTYPE(ctypes.c_int, ctypes.POINTER(S))(lambda n: n)(S(5, 0.5))

def test3():
    pywintypes.PYFUNCTYPE(ctypes.c_int, ctypes.POINTER(S))(lambda n: n)(s)

s = S(5, 0.5)

def test4():
    pywintypes.PYFUNCTYPE(ctypes.c_int, ctypes.POINTER(S))(lambda n: n)(s)
