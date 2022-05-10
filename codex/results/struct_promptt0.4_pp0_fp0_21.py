import _struct
# Test _struct.Struct.__reduce__

import pickle

class S(object):
    def __init__(self, format):
        self.format = format
        self.size = _struct.calcsize(format)
        self.unpack = _struct.Struct(format).unpack
        self.pack = _struct.Struct(format).pack

def test_reduce():
    for code in 'cbB?hHiIlLqQfd':
        s = S(code)
        s2 = pickle.loads(pickle.dumps(s))
        assert s.format == s2.format
        assert s.size == s2.size
        assert s.unpack(s.pack(42)) == s2.unpack(s2.pack(42))

def test_reduce_endian():
    for code in 'cbB?hHiIlLqQfd':
        s = S('<' + code)
        s2 = pickle.loads(pickle.dumps(s))
        assert s.format == s2.format
        assert s.size ==
