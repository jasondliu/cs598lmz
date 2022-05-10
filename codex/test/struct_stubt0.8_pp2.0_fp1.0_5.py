from _struct import Struct
s = Struct.__new__(Struct)
s.size = len(b'\x01\x02\x03')
s.format = 'c'
s.pack = lambda x, y: x
s.unpack = lambda x, y: (x,)
s.unpack_from = lambda x, y: (x,)
s.iter_unpack = lambda x, y: iter((x,))

_sizeof_short = Struct('=h').size
_sizeof_int = Struct('=i').size
_sizeof_long = Struct('=l').size

def sizeof_short(self):
    return _sizeof_short
def sizeof_int(self):
    return _sizeof_int
def sizeof_long(self):
    return _sizeof_long


def bufs_from_pyobj(bufs):
    if not isinstance(bufs, tuple):
        if bufs is None:
            return ()
        else:
            bufs = (bufs,)
    bufs = tuple(memoryview(x) for x in bufs)
    return bufs

