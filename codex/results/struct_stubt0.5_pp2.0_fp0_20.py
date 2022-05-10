from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)

# Output:
# b'\x00\x00\x00\x01'

# This is equivalent to the following:

import struct
struct.pack('>i', 1)

# Output:
# b'\x00\x00\x00\x01'

# The first argument is the format, which will be the same as that used in the struct module.
# The second argument is the data, which will be a tuple.
# For more details on the format, see the documentation for the struct module.


# The Struct class also has a size attribute, which gives the size of the struct in bytes.

# Example:

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# Output:
# 4


# The unpack method unpacks the data from a bytes object.
# The first argument is the format, which will be the same as that used in the struct module.
# The second argument is the data, which
