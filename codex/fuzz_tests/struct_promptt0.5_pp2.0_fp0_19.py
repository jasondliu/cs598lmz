import _struct
# Test _struct.Struct

import struct
import sys

s = _struct.Struct("i")
args = (1,)
buf = s.pack(*args)
print repr(buf)
print s.unpack(buf)

buf = s.pack_into(buf, 0, *args)
print repr(buf)
print s.unpack_from(buf, 0)

buf = buffer(buf)
print repr(buf)
print s.unpack_from(buf, 0)

# test error messages
try:
    s.pack(1, 2)
except TypeError, msg:
    print msg
try:
    s.unpack("")
except struct.error, msg:
    print msg
try:
    s.unpack("x")
except struct.error, msg:
    print msg
try:
    s.unpack("xxxx")
except struct.error, msg:
    print msg

# test struct objects with non-native byte order
if sys.byteorder == "little":
    codes = ">"
else:
    codes = "<"

for code in codes:
