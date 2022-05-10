import _struct
# Test _struct.Struct

print 'Unaligned test'

# Create an unaligned struct
S = _struct.Struct('<i')

# Get the size
print S.size

# Pack a number
print S.pack(1)

# Unpack a number
print S.unpack(S.pack(1))

# Try packing a string
try:
    S.pack('a')
except TypeError:
    print 'Caught TypeError'

# Try unpackin a string
try:
    S.unpack('a')
except TypeError:
    print 'Caught TypeError'

# Try passing too many arguments
try:
    S.pack(1, 2)
except TypeError:
    print 'Caught TypeError'

# Try passing too many arguments
try:
    S.unpack('a', 'b')
except TypeError:
    print 'Caught TypeError'

# Try passing too few arguments
try:
    S.pack()
except TypeError:
    print 'Caught TypeError'

# Try passing too few arguments
try:
    S
