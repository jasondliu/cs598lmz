from _struct import Struct
s = Struct.__new__(Struct)
assert_raises(AttributeError, s.__call__, '?')

# --
# Subclassing test

class StructTest(Struct, object): pass
st = StructTest('?')
assert_equal(st.size, struct.calcsize('?'))

# check for bad subclassing
class C(Struct):
    def __init__(self, format):
        pass
assert_raises(TypeError, C(''))

class D(Struct, object):
    def __init__(self, format):
        pass
assert_raises(TypeError, D(''))

def test_clone(st, m):
    other = st.__class__(st)
    assert_equal(st.size, other.size)
    assert_equal(st.format, other.format)
    assert_equal(m.size, other.size)
    assert_equal(m.format, other.format)

    # check that assignment does not change the instance
    other = st
    assert_equal(st.size, other.size)
    assert_equal
