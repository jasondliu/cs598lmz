import _struct
# Test _struct.Struct object's methods.
#http://docs.python.org/3/library/struct.html
struct_size = _struct.calcsize('fff')
fields = ('x', 'y', 'z')
coord = _struct.Struct('fff')

filter = format = '<xyz'
_struct.pack() # https://docs.python.org/3/library/struct.html#struct.pack

xyz = (0.0, 1.0, 2.0)
pack_data = _struct.pack(filter + format, *xyz)  # _struct.pack()
import struct
struct.pack('<fff', *xyz)
struct.unpack(filter + format, pack_data)

# errors.
struct.unpack(filter + format + 'fff', pack_data)
struct.unpack(filter + format, pack_data + pack_data)

import copy
a = copy.deepcopy(struct_size)
a *= 2
struct.unpack(filter + format, pack_data * a)
struct.unpack(filter + format * a, pack
