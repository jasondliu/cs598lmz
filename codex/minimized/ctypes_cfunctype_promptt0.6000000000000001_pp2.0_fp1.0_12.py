from ctypes import *
def func(i, f, c, s, u, p, z, q, r, h, v, w, t, x):
    print(i, f, c, s, u, p, z, q, r, h, v, w, t, x)
cfunc = CFUNCTYPE(c_int)()
cfunc()
