import _struct
# Test _struct.Struct with other format characters.
print(_struct.Struct('c').size)
print(_struct.Struct('b').size)
print(_struct.Struct('B').size)
print(_struct.Struct('h').size)
print(_struct.Struct('H').size)
print(_struct.Struct('i').size)
print(_struct.Struct('I').size)
print(_struct.Struct('l').size)
print(_struct.Struct('L').size)
print(_struct.Struct('q').size)
print(_struct.Struct('Q').size)
print(_struct.Struct('n').size)
print(_struct.Struct('N').size)
print(_struct.Struct('f').size)
print(_struct.Struct('d').size)
print(_struct.Struct('s').size)
print(_struct.Struct('p').size)
print(_struct.Struct('P').size)
# Test _struct.Struct with other format characters and repeat counts.
print(_struct.Struct('cc').size)
print(_struct.Struct('bb').size)
print(_struct.Struct('BB').size)
print(_struct.
