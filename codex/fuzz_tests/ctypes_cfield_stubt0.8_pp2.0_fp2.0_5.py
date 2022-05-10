import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Array(object):
    """Accessible as either an array or an attribute.
    """
    def __init__(self, type, length):
        self._type = type
        self._length = length
    def __getattribute__(self, name):
        if name.startswith('_'):
            return object.__getattribute__(self, name)
        if name == 'length':
            return object.__getattribute__(self, '_length')
        if name == 'type':
            return object.__getattribute__(self, '_type')
        assert isinstance(name, (int, long))
        return ctypes.CField(name, self.type, self)

def test_fields():
    a = Array(ctypes.c_int, 4)

    # tuple of names and types
    assert isinstance(a.fields, tuple)
    assert len(a.fields) == a.length

    for i in range(a.length):
        assert a.fields[i][0] == str(i)
        assert a.fields[
