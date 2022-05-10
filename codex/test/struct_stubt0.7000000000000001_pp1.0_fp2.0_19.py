from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(">f")

def unpack_float(v):
    return s.unpack(v)[0]

def pack_float(f):
    return s.pack(f)

def unpack_float_list(l):
    return [unpack_float(v) for v in l]

def unpack_float_list_list(l):
    return [unpack_float_list(v) for v in l]

def unpack_float_list_list_list(l):
    return [unpack_float_list_list(v) for v in l]


#=================================================
# "Batch" data types

class BatchKey(object):
    """
    A key that may be used to change the batch configuration.

    This only works if we're using the batch server and it is
    using the "batch" protocol.

    The key is a tuple of strings.  Each UI component has its own
    special key, for example for the "Main" component it is
    ("Main", "").
    """
