from _struct import Struct
s = Struct.__new__(Struct)
s.size = Struct.size
def encode(value):
    return s.pack(value)

def decode(buffer):
    return s.unpack(buffer)[0]
</code>
The encoding/decoding is done by an other program.
The problem is that is the data block become bigger than 65535 byte, the decoding function will fail.
I guess because of the field size. But I don't get how to change that.
I tried:
<code>s = Struct('&gt;H')
s = Struct('&gt;I')
s = Struct('I')
</code>
All of them failed.
If I change the encoding to:
<code>def encode(value):
    return value.encode('utf-8')

def decode(buffer):
    return buffer.decode('utf-8')
</code>
It works, but the client is slow. I mean the encoding is done with 80KB/s and the decoding with 100KB/s.

