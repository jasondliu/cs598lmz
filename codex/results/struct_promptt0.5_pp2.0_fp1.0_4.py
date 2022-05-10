import _struct
# Test _struct.Struct

fmt = 'h'
s = _struct.Struct(fmt)
if s.size != _struct.calcsize(fmt):
    print('size error')

if s.pack(*range(s.size)) != struct.pack(fmt, *range(s.size)):
    print('pack error')

if s.unpack(s.pack(*range(s.size))) != tuple(range(s.size)):
    print('unpack error')

try:
    s.pack()
except TypeError:
    pass
else:
    print('pack error')

try:
    s.unpack(b'')
except struct.error:
    pass
else:
    print('unpack error')

try:
    s.unpack(b'x')
except struct.error:
    pass
else:
    print('unpack error')

try:
    s.pack(1, 2)
except TypeError:
    pass
else:
    print('pack error')

try:
    s.unpack(b'
