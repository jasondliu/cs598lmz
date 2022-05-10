import _struct
# Test _struct.Struct

# Functions which don't use a format string
# but have a fixed typecode

struct_classes = [
        _struct.Struct]

for struct_class in struct_classes:
    s = struct_class('a')
    print(s.size)
    print(s.pack(ord('a')))
    print(s.unpack(b'a'))
    print(s.unpack_from(b'a'))
    print(s.pack_into(b'b', 0, ord('a')))

for op in ['@=', '@<', '@>', '@!']:
    try:
        s = struct_class(op)
    except ValueError:
        print('pass')
    else:
        print('fail')

s = struct_class('x')
try:
    s.unpack(b'x')
except TypeError:
    print('pass')
else:
    print('fail')
