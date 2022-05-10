import _struct
# Test _struct.Struct.format and _struct.calcsize(format)
# First argument to calcsize is a string, not a Struct object

# All integer formats
print 'integer formats'
for format in 'b', 'h', 'i', 'l', 'q':
    print format, ':', _struct.calcsize(format)

# All float formats
print 'float formats'
for format in 'f', 'd':
    print format, ':', _struct.calcsize(format)

# Empty string
print 'empty string :', _struct.calcsize('')

# Check endian symbols
print 'endian symbols'
print '>b :', _struct.calcsize('>b')
print '=b :', _struct.calcsize('=b')
print '<b :', _struct.calcsize('<b')
print '@b :', _struct.calcsize('@b')

# Check that format argument must be a string
print 'format argument must be a string'
try:
    _struct.calcsize(None)
except Type
