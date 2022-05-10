from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'BBBBBBBB'
s.size = 8

def _unpack(fmt, data):
    s.format = fmt
    return s.unpack(data)

def _pack(fmt, *data):
    s.format = fmt
    return s.pack(*data)

def _unpack_from(fmt, data, offset):
    s.format = fmt
    return s.unpack_from(data, offset)

def _pack_into(fmt, buf, offset, *data):
    s.format = fmt
    return s.pack_into(buf, offset, *data)

def byteswap(data):
    '''Reverse the byte order of a string'''
    if not isinstance(data, basestring):
        raise TypeError

    if len(data) % 2 != 0:
        raise ValueError('byteswap requires an even-sized string')

    return ''.join(reversed(data))

def ntohs(x):
    return byteswap(x)

