import _struct
# Test _struct.Struct.__repr__ and .__eq__

import pickle
import copy

class S(object):
    def __eq__(self, other):
        return isinstance(other, S)
    def __reduce__(self):
        return (self.__class__, ())

data = []
for format in _struct.FORMATS.split(','):
    # test the format itself
    s = _struct.Struct(format)
    data.append(s)
    # test a simple type that can be returned
    t = type('test_struct_%s' % format, (S,), {})
    s = _struct.Struct(format, t)
    data.append(s)

# Test pickling and unpickling
for s in data:
    p = pickle.dumps(s)
    t = pickle.loads(p)
    assert s == t
    assert repr(s) == repr(t)
    assert s.format == t.format
    assert s.size == t.size
