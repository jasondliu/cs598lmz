import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(10.0)
    y = ctypes.c_float(10.0)
    _fields_ = [('x', ctypes.c_float), ('y', ctypes.c_float)]

# This is from ctypes.test.test_c.
def write_int(addr, value):
    ctypes.memset(addr, value, 4)

def main():
    s = S()
    a = ctypes.addressof(s)
    print s.x
    write_int(a, 0x12345678)
    print s.x

main()
