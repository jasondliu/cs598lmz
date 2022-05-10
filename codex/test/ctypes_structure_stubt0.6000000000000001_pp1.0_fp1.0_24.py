import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()
    y = ctypes.c_long()

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.c_long), ('y', ctypes.c_long)]

def main():
    print(ctypes.sizeof(S))
    print(ctypes.sizeof(T))

main()
