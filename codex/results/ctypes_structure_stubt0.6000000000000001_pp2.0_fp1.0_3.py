import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def get_sizeof(obj):
    return ctypes.sizeof(type(obj))

if __name__ == '__main__':
    print(get_sizeof(10))
    print(get_sizeof(True))
    print(get_sizeof(S()))
</code>

