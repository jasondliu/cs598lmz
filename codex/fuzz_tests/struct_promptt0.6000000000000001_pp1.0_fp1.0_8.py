import _struct
# Test _struct.Struct

def check_sizeof(fmt, size):
    s = _struct.Struct(fmt)
    if s.size != size:
        raise Exception("%s: sizeof != %s" % (fmt, size))

def check_unpack(fmt, data, expected):
    s = _struct.Struct(fmt)
    res = s.unpack(data)
    if res != expected:
        raise Exception("%s: %s != %s" % (fmt, res, expected))

def check_unpack_from(fmt, data, expected, offset=0):
    s = _struct.Struct(fmt)
    res = s.unpack_from(data, offset)
    if res != expected:
        raise Exception("%s: %s != %s" % (fmt, res, expected))

def check_pack(fmt, data, expected):
    s = _struct.Struct(fmt)
    res = s.pack(data)
    if res != expected:
        raise Exception("%s: %s != %s
