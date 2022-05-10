import ctypes

class S(ctypes.Structure):
    x = ctypes.ARRAY(ctypes.c_int, 3)
    y = ctypes.c_ushort
    z = ctypes.ARRAY(ctypes.c_byte, 2)

p = ctypes.POINTER(S)()
#
ctypes.POINTER(S).from_address(id(p)).contents.x[0] = 1
ctypes.POINTER(S).from_address(id(p)).contents.x[1] = 2
ctypes.POINTER(S).from_address(id(p)).contents.x[2] = 3
ctypes.POINTER(S).from_address(id(p)).contents.y = 4
ctypes.POINTER(S).from_address(id(p)).contents.z[0] = 5
ctypes.POINTER(S).from_address(id(p)).contents.z[1] = 6

for i in range(0, id(p) + 100, 4):
    print(hex(i), ":", ''.join(r"\x{:02x}
