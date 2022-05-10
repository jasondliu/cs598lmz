from _struct import Struct
s = Struct.__new__(Struct) # create a new Struct object
s.__init__('i')             # init with a format string
s.pack(10)                  # pack an int into a bytes object
s.unpack(b'\x0a\x00\x00\x00') # unpack a bytes object
s.unpack_from(b'\x0a\x00\x00\x00', 0) # unpack from a buffer

#
#
#

import sys
import struct

def read_struct(filename, format):
    """
    Read a file and unpack its contents using the given format.
    """
    with open(filename, 'rb') as f:
        return struct.unpack(format, f.read())

#
#
#

import sys
import struct

def read_struct(filename, format):
    """
    Read a file and unpack its contents using the given format.
    """
    with open(filename, 'rb') as f:
        return struct.unpack(format, f.read())

