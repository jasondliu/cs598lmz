import _struct
# Test _struct.Struct with the struct module
from struct import calcsize

def test(fmt):
    print 'fmt:', fmt
    s = _struct.Struct(fmt)
    print 'calcsize:', calcsize(fmt)
    print 'size:', s.size
    print 'format:', s.format
    print 'pack:', s.pack(1, 2, 3)
    print 'unpack:', s.unpack(_struct.pack(fmt, 1, 2, 3))
    print 'iter unpack:', list(s.iter_unpack(_struct.pack(fmt, 1, 2, 3)))
    print 'unpack_from:', s.unpack_from(_struct.pack(fmt, 1, 2, 3), 0)
    print 'iter unpack_from:', list(s.iter_unpack_from(_struct.pack(fmt, 1, 2, 3), 0))
    print 'pack_into:',
    buf = array('B', '12345678')
    print 'before:', buf
    s.pack_into
