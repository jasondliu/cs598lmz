import _struct
# Test _struct.Struct() arg
print(_struct.Struct('i').size)
# 2
print(_struct.Struct('L').size)
# 4
print(_struct.Struct('q').size)
# 8
print(_struct.Struct('Q').size)
# 8
