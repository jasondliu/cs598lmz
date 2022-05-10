import _struct
# Test _struct.Struct

fmt = 'bBhHiIlLqQfdspP'

for code in fmt:
    s = _struct.Struct(code)
    print(type(s), s, repr(s))

print(_struct.Struct('i')(12))

print(_struct.Struct('i')('abc'))

try:
    _struct.Struct()
except TypeError:
    print('TypeError')
except ValueError:
    print('ValueError')

try:
    _struct.Struct(1)
except TypeError:
    print('TypeError')
except ValueError:
    print('ValueError')

try:
    _struct.Struct('')
except TypeError:
    print('TypeError')
except ValueError:
    print('ValueError')

try:
    _struct.Struct('abc')
except TypeError:
    print('TypeError')
except ValueError:
    print('ValueError')

try:
    _struct.Struct('@')
except TypeError:
    print('TypeError')
except ValueError:
   
