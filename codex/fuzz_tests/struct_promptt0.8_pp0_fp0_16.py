import _struct
# Test _struct.Struct
# XXX should make more tests...
def test_struct():
    # Check alignment
    s = _struct.Struct('i')
    assert s.size == _struct.calcsize('i')
    #warnings.filterwarnings('error', '', RuntimeWarning)
    raises(_struct.error, _struct.Struct, 'iii')

# More tests
def test_opt_arg():
    """
    def pack(self, fmt, v1, v2=0, v3=0):
        return _struct.pack(fmt, v1, v2, v3)
    s = _struct.Struct('hhi')
    res = s.pack('abc', 1, 2, 3)
    res = s.pack(1, 2, 3)
    res = s.pack(1, 2)
    res = s.pack(1)
    """
    pass

def test_struct_error():
    """
    s = _struct.Struct('')
    raises(_struct.error, s.pack)
    raises(_struct.error, _struct.Struct, '
