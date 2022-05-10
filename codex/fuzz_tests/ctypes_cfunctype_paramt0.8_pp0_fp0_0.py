import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def cos(val):
  with open('libcos.so', 'rb') as f:
    dll = ctypes.CDLL(None, f)
    func = FUNTYPE(('cos', dll))
    return func(val)

print cos(0.5)
