import _struct
# Test _struct.Struct.unpack_from()

import _struct
import array
import sys

# Test various types of structs

# Test structs with alignment
for align in range(1, 9):
    s = _struct.Struct('%dx' % align)
    a = array.array('b', b'\0' * align)
    s.unpack_from(a, 0)

# Test structs with non-native size
for size in range(1, 9):
    s = _struct.Struct('%ds' % size)
    a = array.array('b', b'\0' * size)
    s.unpack_from(a, 0)

# Test structs with non-native alignment
for align in range(1, 9):
    s = _struct.Struct('%dx' % align)
    a = array.array('b', b'\0' * align)
    s.unpack_from(a, 0)

# Test structs with non-native size and alignment
for size in range(1, 9):
    for align in range(1,
