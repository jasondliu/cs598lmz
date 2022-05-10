import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p
    y = ctypes.c_void_p
    z = ctypes.c_void_p

def main():
    libc = ctypes.CDLL("libc.so.6")
    s = S()

    libc.printf("%p %p %p %p %p\n", s.x, s.y, s.z, ctypes.addressof(s), ctypes.addressof(s.x))

main()
</code>

