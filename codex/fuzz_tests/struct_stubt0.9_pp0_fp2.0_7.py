from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('!i4sh')
s.pack(1,2,3,4)

data = s.pack(12345,b'python',54321,b'python')
import struct
st = struct.Struct('!i4sh')
st.pack(12345,b'python',54321,b'python')
st.unpack(data)

import struct
import itertools
binary_stdin = open('foo.bin','rb')
data = binary_stdin.read()
i = itertools.count()
s = struct.Struct('!i4sh')
while True:
    try:
        unpacked = s.unpack_from(data,next(i)*s.size)
    except struct.error:
        break
    print(unpacked)

s = struct.Struct('=i4sh')
s.pack(123,b'abcd',543)

a = 123
a = 123.456
a = 123+4j
a = b'abc'
a = {'foo':None,'bar
