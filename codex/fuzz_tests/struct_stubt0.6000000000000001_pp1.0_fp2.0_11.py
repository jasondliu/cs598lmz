from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('!B')

with open('test.bin', 'rb') as f:
    data = f.read()

for i in range(0, len(data), s.size):
    buffer = data[i:i+s.size]
    value = s.unpack(buffer)[0]
    print(value)
</code>
Prints:
<code>10
20
30
40
50
</code>

EDIT: You can also use the <code>struct</code> module to read binary data.
<code>import struct

with open('test.bin', 'rb') as f:
    while True:
        data = f.read(1)
        if data:
            value = struct.unpack('!B', data)[0]
            print(value)
        else:
            break
</code>

