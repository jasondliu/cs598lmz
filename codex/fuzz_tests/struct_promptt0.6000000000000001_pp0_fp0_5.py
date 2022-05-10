import _struct
# Test _struct.Struct.

# Basic usage.
struct = _struct.Struct('i')
print struct.pack(1)
print struct.unpack(struct.pack(1))

# Overflow.
try:
    print struct.unpack('\xff'*4)
except Exception, e:
    print e

# Wrong size.
try:
    print struct.unpack('x')
except Exception, e:
    print e

# Long format.
print _struct.calcsize('cccccccccccccccc')
print _struct.calcsize('cccccccccccccccccc')

# Invalid format.
try:
    print _struct.calcsize('ccccccccccccccccc')
except Exception, e:
    print e

# Format with '0'.
print _struct.calcsize('0')
print _struct.Struct('0').pack()

# Format with 'P'.
print _struct.calcsize('P')
print _struct.Struct('P').pack(1)

# Format with 'p'.
print _struct
