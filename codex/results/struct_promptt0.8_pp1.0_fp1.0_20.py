import _struct
# Test _struct.Struct objects with standard code argument
values = (1, 2.0, 3.0+0.0j)
for code in 'cbBhHiIlLfd':
    format = '<' + code
    x = _struct.Struct(format)
    s = x.pack(*values)
    y = _struct.Struct(format)
    z = y.unpack(s)
    print repr(s), z
print repr(x.pack(1000000000))

# Test with format string and optional size
format = '<2i9sh'
x = _struct.Struct(format)
s = x.pack(*values)
y = _struct.Struct(format)
z = y.unpack(s)
print repr(s), z

# Produce an error
try:
    _struct.Struct('ci')
except _struct.error, msg:
    print msg
try:
    _struct.Struct('<1c')
except _struct.error, msg:
    print msg

# Issue #3761: Incorrect alignment of nested Structs in the packer
import bin
