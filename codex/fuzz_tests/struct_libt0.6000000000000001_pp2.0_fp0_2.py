import _struct

#------------------------------------------------------------------------------

def pack(format, *args):
    """
    Return a string containing the values v1, v2, ... packed according to the
    given format.
    """
    return _struct.pack(format, *args)

def unpack(format, string):
    """
    Unpack the string (presumably packed by pack(format, ...)) according to the
    given format.  The result is a tuple even if it contains exactly one item.
    """
    return _struct.unpack(format, string)

def unpack_from(format, string, offset=0):
    """
    Unpack the buffer according to the given format.  The result is a tuple
    even if it contains exactly one item.  The buffer's size in bytes must be at
    least offset + calcsize(format).
    """
    return _struct.unpack_from(format, string, offset)

def iter_unpack(format, buffer):
    """
    Return an iterator yielding tuples unpacked from the given bytes.  The
    buffer's size in bytes must be
