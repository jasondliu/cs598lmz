import _struct

def to_array(val):
    as_list = []
    while val != 0:
        as_list.append(val&0xff)
        val = val >> 8
    return as_list

def to_int(bytes_):
    as_int = 0
    exp = 0;
    for byte in bytes_:
        as_int += (byte << exp)
        exp += 8
    return as_int

class Packer(object):
    """ Packs integers into a bytestream """
    def __init__(self):
        pass

    def pack(self, fmt, val):
        format_ = fmt.split('-')[0]
        size = int(fmt.split('-')[1])
        method = 'pack_' + format_
        pack_method = getattr(self, method)
        return pack_method(size, val)

    def pack_uint(self, size, val):
        val = to_array(val)
        return _struct.pack('>' + ('B'*size), *val)

