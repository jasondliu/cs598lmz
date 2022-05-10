import _struct
# Test _struct.Struct

# Test the basic constructor
s = _struct.Struct('i')
assert s.format == 'i'
assert s.size == _struct.calcsize('i')

# Test the __new__ method
s = _struct.Struct.__new__(_struct.Struct, 'i')
assert s.format == 'i'
assert s.size == _struct.calcsize('i')

# Test the from_param method
class S(_struct.Struct):
    _length_ = 4
    _pack_ = 1
    _struct_ = 'i'
    def __init__(self, arg):
        self.arg = arg
    def from_param(cls, arg):
        return cls(arg)
    from_param = classmethod(from_param)

s = S(42)
assert s.arg == 42
assert s.format == 'i'
assert s.size == _struct.calcsize('i')

# Test the __len__ method
assert len(s) == _struct.calcsize('i')

# Test the __str__
