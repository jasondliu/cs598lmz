import _struct
# Test _struct.Struct

fmt = 'hhl'
s = _struct.Struct(fmt)
buf = s.pack(1, 2, 3)
t = s.unpack(buf)
print(t)
s = _struct.Struct('@%c' % fmt)
buf = s.pack(1, 2, 3)
t = s.unpack(buf)
print(t)

fmt = 'hhl'
s = _struct.Struct(fmt)
buf = s.pack(1, 2, 3)
t = _struct.unpack(fmt, buf)
print(t)

fmt = 'hhl'
s = _struct.Struct(fmt)
buf = s.pack(1, 2, 3)
t = _struct.unpack('@%c' % fmt, buf)
print(t)

# Test error handling

import sys

try:
    s.unpack(buf + '\0')
except Exception as e:
    print(type(e), e)
