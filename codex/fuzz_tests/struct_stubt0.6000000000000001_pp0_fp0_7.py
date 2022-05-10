from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("i",None,2)

with open("test.bin", "rb") as f:
    data = f.read()

r = s.unpack(data)
print(r)
</code>


A:

In python 2, you can use <code>struct.unpack_from</code> to read from a string at a given offset:
<code>import struct
with open("test.bin", "rb") as f:
    data = f.read()

offset = 0
while offset &lt; len(data):
    r = struct.unpack_from('i', data, offset)[0]
    print(r)
    offset += 4
</code>

