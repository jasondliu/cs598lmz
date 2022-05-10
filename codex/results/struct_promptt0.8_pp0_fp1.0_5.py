import _struct
# Test _struct.Struct with alignment, if it's present.
try:
    _struct.Struct('@i')
    _is_64bit = (1 << 32) == 0
except TypeError:
    pass
else:
    _s_long = _struct.Struct('i' if _is_64bit else 'l')
    _s_ulong = _struct.Struct('I' if _is_64bit else 'L')
# Else, assume we're on a 32-bit machine.


def unpack(typecode, data):
    """
    unpack(typecode, data) -> (value, newpos)

    Unpack from the data starting at position pos, according to the format
    string typecode. Return a tuple containing the converted value an the
    new position in the data.

    The typecode argument must be a bytes object of length 1.
    """
    assert isinstance(typecode, bytes) and len(typecode) == 1
    if typecode in ('c', 's'):
        return (data.decode('latin1'), data[1:])
    size = _calcsize
