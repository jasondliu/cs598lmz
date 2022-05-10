import _struct
# Test _struct.Struct.

import _struct

# Test all standard formats.

for code in 'bBhHiIlLfd':
    fmt = _struct.Struct(code)
    print fmt.format, fmt.size, repr(fmt.pack(42)), repr(fmt.unpack(fmt.pack(42)))

# Test native size and alignment.

print _struct.calcsize('P')
print _struct.calcsize('Pii')
print _struct.calcsize('Pi')

# Test non-native size and alignment.

print _struct.calcsize('=P')
print _struct.calcsize('=Pii')
print _struct.calcsize('=Pi')

# Test standard error messages.

try:
    _struct.calcsize('z')
except _struct.error, msg:
    print msg

try:
    _struct.calcsize('Pz')
except _struct.error, msg:
    print msg

try:
    _struct.pack('PiiP', (1, 2))
except TypeError
