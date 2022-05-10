import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
lib = ctypes.CDLL('./mylib.so')
func = FUNTYPE(('mycfunc', lib))
print(func(1.0))
print(func(2.0))
print(func(3.0))

print("\n\n")

# ctypesでCの関数を呼び出す２
functype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
lib = ctypes.CDLL('./mylib.so')
func = functype(('mycfunc', lib))
print(func(1.0))
print(func(2.0))
print(func(3.0))

print("\n\n")

# ctypesでCの関数を呼び出す３
def mycfunc(x):
    func = ctypes.CDLL('./mylib.so').mycfunc
    func.restype = c
