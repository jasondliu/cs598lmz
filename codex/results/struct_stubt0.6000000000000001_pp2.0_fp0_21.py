from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<i'
s.size = 4

# struct.error: 'i' format requires -2147483648 <= number <= 2147483647



# print(s.pack(*(2 ** 31 - 1,)))
# print(s.pack(*(2 ** 31,)))
# print(s.pack(*(-2 ** 31,)))
# print(s.pack(*(-2 ** 31 - 1,)))

# i = 2 ** 31 - 1
# print(i.to_bytes(4, 'big', signed=True))
# i = 2 ** 31
# print(i.to_bytes(4, 'big', signed=True))
# i = -2 ** 31
# print(i.to_bytes(4, 'big', signed=True))
# i = -2 ** 31 - 1
# print(i.to_bytes(4, 'big', signed=True))

# b'\x7f\xff\xff\xff'
# b'\x80\x00\x00\x00'
# b'\x80\
