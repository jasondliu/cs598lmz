import _struct
# Test _struct.Struct
struct = _struct.Struct("hhl")
data = struct.pack(1, 2, 3)
print(data)
print(struct.unpack(data))
struct.unpack_from(data)
</code>
Output:
<code>b'\x01\x00\x02\x00\x03\x00\x00\x00'
(1, 2, 3)
</code>

