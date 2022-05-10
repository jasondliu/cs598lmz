from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

# _struct.Struct.__new__() takes the format string as an argument and returns a new Struct object.
# The format string uses the same codes as those used by the pack() and unpack() functions.
# The Struct.__init__() method then initializes the format string.

# A Struct object operates exactly like the pack() and unpack() functions.
# The only difference is that it requires an extra step to create the object.
# The advantage is that it can be used repeatedly for multiple calls and has the added benefit of being more self-documenting.

import struct

def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    '''
    record_struct = struct.Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))

# The write_records() function takes a format string, a sequence of tuples, and a file object.
# It creates a Struct object and uses it to write
