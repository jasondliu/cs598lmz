import _struct
# Test _struct.Struct.__repr__
print(_struct.Struct('i').__repr__())
print(_struct.Struct('i').__repr__(1))
print(_struct.Struct('i').__repr__(1, 2))
print(_struct.Struct('i').__repr__(1, 2, 3))
print(_struct.Struct('i').__repr__(1, 2, 3, 4))
# Test _struct.Struct.__str__
print(_struct.Struct('i').__str__())
print(_struct.Struct('i').__str__(1))
print(_struct.Struct('i').__str__(1, 2))
print(_struct.Struct('i').__str__(1, 2, 3))
print(_struct.Struct('i').__str__(1, 2, 3, 4))
# Test _struct.Struct.format
print(_struct.Struct('i').format)
print(_struct.Struct('i').format(1))
print(_struct.Struct('i').format(1, 2))
print(_struct.Struct('i').format(1, 2, 3))
