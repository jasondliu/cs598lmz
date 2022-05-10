from _struct import Struct
s = Struct.__new__(Struct)
print(s)
print(s.size)

############
# Reference
############

import _struct
print(_struct.__doc__)
help(_struct)

##########################
# Example: Packing Objects
##########################

# pack into bytes
import struct
b = struct.pack('>hhl', 1, 2, 3)
print(b)

# unpack into objects
import struct
b = struct.pack('>hhl', 1, 2, 3)
values = struct.unpack('>hhl', b)
print(values)

##########################
# Example: Unpack Integers
##########################

import struct
b = struct.pack('>hhl', 1, 2, 3)
print(b)
i1 = struct.unpack('>H', b[:2])
print(i1)
i2 = struct.unpack('>H', b[2:4])
print(i2)
i3 = struct.unpack('>L', b[4:])
print(i3)

#################################
# Example:
