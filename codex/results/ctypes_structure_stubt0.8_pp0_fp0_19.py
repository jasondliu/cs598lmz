import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint16()
    y = ctypes.c_uint16()

def main():
    s = S()
    s.x = 0x1234
    #s._fields_ = [('y', s.y), ('x', s.x)]
    print(s.x)
    print(s.y)
    print(hex(ctypes.addressof(s)))

if __name__ == '__main__':
    main()
</code>

