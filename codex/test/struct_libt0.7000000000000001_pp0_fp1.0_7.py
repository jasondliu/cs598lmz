import _struct

def _pack_int(num, bigendian):
    """
    Pack a non-negative integer into its packed representation.
    """
    if num < 256:
        return chr(num)
    elif num < 65536:
        if bigendian:
            return '\x00' + chr(num)
        else:
            return chr(num) + '\x00'
    elif num < 4294967296:
        if bigendian:
            return '\x00\x00' + chr(num) + '\x00'
        else:
            return '\x00' + chr(num) + '\x00\x00'
    else:
        raise OverflowError("integer does not fit 'I' format")

def _unpack_int(data, bigendian):
    """
    Unpack packed integer from a string.
    """
    if len(data) == 1:
        return ord(data)
