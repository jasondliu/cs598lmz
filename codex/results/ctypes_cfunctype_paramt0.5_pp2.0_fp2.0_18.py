import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)

libc = ctypes.CDLL('./libc.so')
libc.f.restype = ctypes.c_int
libc.f.argtypes = [ctypes.c_int]
f = libc.f

def f_py(x):
    return x+1

f_c = FUNTYPE(f)

print(f_py(1))
print(f_c(1))

import pyximport
pyximport.install()
import libc_cy
print(libc_cy.f(1))

# https://stackoverflow.com/questions/103628/naming-convention-for-c-c-variables-and-functions-with-underscore-prefixed
# https://stackoverflow.com/questions/3448341/python-ctypes-and-c-library-function-with-underscore-prefix
# https://stackoverflow.com/questions/29453908/how-to-call-c-fun
