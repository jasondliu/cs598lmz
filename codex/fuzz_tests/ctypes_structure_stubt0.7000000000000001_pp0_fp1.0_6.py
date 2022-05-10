import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short(0x4321)

print(struct.calcsize(">h"))
print(struct.pack(">h", 0x4321))
print(struct.pack(">h", 0x1234))
print(struct.unpack(">h", b'\x43\x21'))
print(struct.unpack(">h", b'\x12\x34'))
print(ctypes.sizeof(S))
print(ctypes.string_at(ctypes.addressof(S()), ctypes.sizeof(S)))

# Output:
#   2
#   b'\x43\x21'
#   b'\x12\x34'
#   (17185,)
#   (4660,)
#   2
#   b'\x43\x21'
