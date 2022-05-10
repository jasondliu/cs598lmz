import mmap
import struct
import sys

def from_little_endian(data, offset=0, length=0):
    """ Read little endian data from the data string. """
    if offset + length > len(data):
        raise IndexError("Data string not long enough to read %d bytes from offset %d." % (length, offset))
    s = struct.Struct('<' + 'B' * length)
    return s.unpack_from(data, offset)

def to_little_endian(data, offset=0, length=0):
    """ Write little endian data to a data string. """
    if offset + length > len(data):
        raise IndexError("Data string not long enough to write %d bytes to offset %d." % (length, offset))
    s = struct.Struct('<' + 'B' * length)
    s.pack_into(data, offset, *data[offset:offset + length])

def from_big_endian(data, offset=0, length=0):
    """ Read big endian data from the data string. """
   
