import _struct
# Test _struct.Struct()

TestError = _struct.error

# Create template
s = _struct.Struct('hhl')

# Create buffer

b = _struct.pack('hhl', 1, 2, 3)

m = s.unpack(b)

if m != (1, 2, 3):
    raise TestError, 'unpack error'

b = s.pack(1, 2, 3)

if b != _struct.pack('hhl', 1, 2, 3):
    raise TestError, 'pack error'

if s.size != 8:
    raise TestError, 'size error'

if s.format != 'hhl':
    raise TestError, 'format error'

# All tests done
print '_struct test OK'
