from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda: 8
s.format = 'Q'
s.pack = s.pack_into = Struct.pack
s.unpack = s.unpack_from = Struct.unpack

def get_int(data, offset, size=8):
    return int(s.unpack(data[offset:offset+size])[0])

def read_int(f, size=8):
    return get_int(f.read(size), 0, size)

def _format_pdb(v):
    return "pdb://{}".format(v)

def _format_addr(v):
    return "{:016x}".format(v)

def _format_addr_u(v):
    return "{:016x}".format(v)

def _format_symbol(v):
    return '`{}`'.format(v)

def _format_module(v):
    return '`{}`'.format(v)

def _format_name(v):
    return v.decode("utf-8")
