from _struct import Struct
s = Struct.__new__(Struct)
setattr(s, 'format', 'I 2s f')
s.size = s.calcsize()
print(s.size)
# 12

# Example 3
s = struct.Struct('I 2s f')
packed_data = s.pack(1, b'ab', 2.7)
print(packed_data)
data = s.unpack(packed_data)
print(data)
# (1, b'ab', 2.7)

# Example 4
s = struct.Struct('I 2s f')
with open('data.bin', 'wb') as f:
    f.write(s.pack(1, b'ab', 2.7))
# (1, b'ab', 2.7)

# Example 5
packed_data = b'\x00\x00\x00\x01ab\x00\x00@\x00\x00\x00'
data = s.unpack(packed_data)
print(data)
# (1, b'ab', 2.7)

