import ctypes

class S(ctypes.Structure):
    x = ctypes.ARRAY(ctypes.c_int, 1)(-1)
    y = ctypes.ARRAY(ctypes.c_int, 1)(-1)


if __name__ == "__main__":
    v = ctypes.c_int()
    v.value = 10
    s = S()
    print('v', v.value)
    print('x', s.x.value)
    print('y', s.y.value)
    # no, it doesn't.  v is a "pointer" value. 
    print(isinstance(v, ctypes.c_int), isinstance(s.x, ctypes.c_int)) 
    ctypes.memmove(ctypes.cast(ctypes.addressof(s.x), ctypes.POINTER(ctypes.c_int)), ctypes.addressof(v), ctypes.sizeof(v))
    print('x', s.x.value)
