import ctypes

class S(ctypes.Structure):
    x = ctypes.ARRAY(ctypes.c_int, 1)(-1)
    y = ctypes.ARRAY(ctypes.c_int, 1)(-1)


if __name__ == "__main__":
    v = ctypes.c_int()
    v.value = 10
    s = S()
    print('v', v.value)
