import _struct
# Test _struct.Struct.

import sys

# A single format.

fmt = _struct.Struct('l')

# Compute the size of the format.

if fmt.size != _struct.calcsize('l'):
    print('size test failed')

# Check endianness.

big_endian = (sys.byteorder != 'little')

# Pack and unpack some test values.

pack = fmt.pack
unpack = fmt.unpack

for v in [0, 1, -1, 2**31-1, -2**31, 2**32-1, -2**32, 2**63-1, -2**63]:
    x = pack(v)
    if big_endian:
        if x != _struct.pack('>l', v):
            print('pack test failed')
    else:
        if x != _struct.pack('<l', v):
            print('pack test failed')
    if unpack(x)[0] != v:
        print('unpack test failed')

# A more complex format.

fmt
