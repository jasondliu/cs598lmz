from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
pack = s.pack
unpack = s.unpack

def uint2str(i):
    if i<0:
        raise ValueError("cannot convert negative integer to string")
    hex_string = '%x' % i
    if len(hex_string) & 1:
        hex_string = '0' + hex_string # prepend a 0 if odd length
    return unhexlify(hex_string)

def uint4str(i):
    if i<0:
        raise ValueError("cannot convert negative integer to string")
    hex_string = '%x' % i
    if len(hex_string) & 1:
        hex_string = '0' + hex_string # prepend a 0 if odd length
    if len(hex_string) & 2:
        hex_string = '00' + hex_string # prepend a 00 if length is 2 or 3
    return unhexlify(hex_string)

def uint8str(i):
    if i<0:
        raise ValueError("
