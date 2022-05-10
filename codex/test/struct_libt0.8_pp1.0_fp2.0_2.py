import _struct
import struct


def pack(format, *args):
    """Pack arguments into a string according to the given format.

    The arguments must match the values required by the format exactly.
    See help(struct) for more on format strings.

    The result is the binary data that will be used by unpack() to
    unpack the data.

    """
    return _struct.pack(format, *args)


def unpack(format, string):
    """Unpack from the string (presumably packed by pack(format, ...))
       according to the given format.  The result is a tuple even if
       it contains exactly one item.  The string must contain exactly
       the amount of data required by the format (len(string) must equal
       calcsize(format)).
       See help(struct) for more on format strings.
    """
    return _struct.unpack(format, string)


def calcsize(format):
    return _struct.calcsize(format)
