import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_char
    z = ctypes.c_int
    w = ctypes.c_char

with open(sys.argv[1], "rb") as f:
    print(f.read(ctypes.sizeof(S)))
</code>
The problem is that in this case the <code>y</code> field will be represented by a single byte (the padding is not included).

