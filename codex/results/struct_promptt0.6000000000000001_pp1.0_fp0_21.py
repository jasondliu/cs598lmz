import _struct
# Test _struct.Struct()

# _struct.Struct()
for code in 'bBhHiIlLfd':
    fmt = _struct.Struct(code)
    print(fmt.size)

# _struct.Struct() with a format string
for code in 'bBhHiIlLfd':
    fmt = _struct.Struct('@' + code)
    print(fmt.size)

# _struct.Struct() with a format string
for code in 'bBhHiIlLfd':
    fmt = _struct.Struct('=@' + code)
    print(fmt.size)

try:
    fmt = _struct.Struct('a')
except TypeError:
    print('TypeError')

try:
    fmt = _struct.Struct('<a')
except TypeError:
    print('TypeError')

try:
    fmt = _struct.Struct('@a')
except TypeError:
    print('TypeError')

try:
    fmt = _struct.Struct('=a')
except TypeError:
    print('TypeError')

try:
   
