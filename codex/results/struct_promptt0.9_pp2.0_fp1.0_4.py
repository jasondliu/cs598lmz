import _struct
# Test _struct.Struct
print('Unpacking:', _struct.Struct('i').unpack(b'\x01\x02\x03\x04'))
print('Unpacking:', _struct.Struct('i').unpack(b'\x01\x02\x03\x04')[0])

import struct
# Test struct.Struct
print('Packing:', struct.Struct('i').pack(1))
print('Packing:', struct.Struct('i').pack(1)[0])
print('Packing:', struct.Struct('i').unpack(b'\x01\x02\x03\x04')[0])
print('Packing:', struct.Struct('i').unpack(b'\x01\x02\x03\x04'), '\n')

from _struct import *
from struct import *
# Test Struct
from _struct import Struct as Struct_
from struct import Struct as Struct
print('Packing:', Struct_.pack(Struct('i'), 1))
print('Packing:', Struct_.pack(Struct('i'), 1)[0])
