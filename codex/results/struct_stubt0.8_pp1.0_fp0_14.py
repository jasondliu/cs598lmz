from _struct import Struct
s = Struct.__new__(Struct)
s.format = "<BBBBL"
print("Mapping:", s.format)
print("Size:", s.size)
print("Unpacking:", s.unpack(b'\xff\xfe\x00\x01\x00\x00\x00\x0e'))
print("Packing:", s.pack(1, 2, 3, 4, 5))

print("Unpacking:", s.unpack_from(b'\xff\xfe\x00\x01\x00\x00\x00\x0e\x00\x00\x00\x00', 4))

# 不考虑大小端时
print("Unpacking:", s.unpack_from(b'\xfe\xff\x01\x00\x0e\x00\x00\x00', 1))

# 大小端测试
import sys
if sys.byteorder == "little":
    print("Little-endian platform.")
else:
    print("Big-endian
