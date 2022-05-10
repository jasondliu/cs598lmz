from _struct import Struct
s = Struct.__new__(Struct)
s.size = 4
s._fmt = 'I'
import ctypes
oc = ctypes.pointer(ctypes.c_int())
poc = ctypes.pointer(oc)
import sys
if sys.byteorder == 'big':
    data = bytes.fromhex('01000000')
else:
    data = bytes.fromhex('00000001')
address = data[:s.size]
address, = s.unpack(address)
</code>
still got the error.
So there must be something wrong with the data (from the process) itself.
I put several breakpoints and checked the data from memory view in the process, there all seems correct (byte ordering, value,...) until the moment the data is copied to local variable (from my local var to the data in binary module, it is already changed)
The data is read as a <code>bytes</code> object, and the moment it is passed to the binary module, it is changed which caused the error.
How can I fix this?

Another way, no success either:
<code>data = b'\x00\x00\x
