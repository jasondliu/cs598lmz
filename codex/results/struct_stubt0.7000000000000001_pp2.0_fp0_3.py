from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
s.format = '>I'
s.size = Struct.calcsize(s.format)

def _unpack(data):
    if isinstance(data, bytes):
        return s.unpack(data)[0]
    return data

def _pack(data):
    if isinstance(data, int):
        return s.pack(data)
    return data


def pack(data):
    if isinstance(data, bytes):
        return data
    if isinstance(data, str):
        return data.encode('utf-8')
    if isinstance(data, int):
        return _pack(data)
    if isinstance(data, list):
        return pack_seq(data)
    if isinstance(data, dict):
        return pack_dict(data)
    raise ValueError("Can't pack '{}'".format(type(data)))

def pack_seq(seq):
    return b''.join(pack(elem) for elem in seq)


def pack
