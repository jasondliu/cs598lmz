import _struct
# Test _struct.Struct.__new__

# Test with a valid format string
s = _struct.Struct('i')

# Test with an invalid format string
try:
    _struct.Struct('x')
except ValueError:
    pass
else:
    print('ValueError expected')

# Test with a tuple
try:
    _struct.Struct(('i',))
except TypeError:
    pass
else:
    print('TypeError expected')

# Test with a list
try:
    _struct.Struct(['i'])
except TypeError:
    pass
else:
    print('TypeError expected')

# Test with a dict
try:
    _struct.Struct({'i': 1})
except TypeError:
    pass
else:
    print('TypeError expected')

# Test with a set
try:
    _struct.Struct({'i'})
except TypeError:
    pass
else:
    print('TypeError expected')

# Test with a frozenset
