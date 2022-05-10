from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format', 'i')
s.__setattr__('size', 4)
s.pack = lambda x: pack('i', x)
s.unpack = lambda x: unpack('i', x)[0]
s.unpack_from = lambda x, y: unpack_from('i', x, y)[0]
s.__setattr__('format', 'i')
s.__setattr__('size', 4)

def pack_int(value):
    return s.pack(value)

def unpack_int(buf):
    return s.unpack(buf)

def unpack_int_from(buf, offset):
    return s.unpack_from(buf, offset)

def pack_int_array(array):
    return ''.join([pack_int(elem) for elem in array])

def unpack_int_array(buf):
    return [unpack_int(buf[i*4:i*4+4]) for i in range(len(buf) / 4)]

def unpack
