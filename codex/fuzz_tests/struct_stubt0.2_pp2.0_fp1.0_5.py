from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>2s3s'
s.size = s.calcsize(s.format)

def unpack(data):
    return s.unpack(data)

def pack(data):
    return s.pack(*data)

def unpack_from(data, offset=0):
    return s.unpack_from(data, offset)

def pack_into(data, offset, values):
    return s.pack_into(data, offset, *values)

def calcsize():
    return s.size

def pack_dict(d):
    return pack((d['type'], d['data']))

def unpack_dict(d):
    return {'type': d[0], 'data': d[1]}

def unpack_dict_from(data, offset=0):
    return unpack_dict(unpack_from(data, offset))

def pack_into_dict(d, data, offset):
    return pack_into(data, offset, (d['type'], d['data']))


