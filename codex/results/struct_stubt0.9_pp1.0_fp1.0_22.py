from _struct import Struct
s = Struct.__new__(Struct)
s.s = 'i?h'
s._format_ = 'i?h'
#s.s = 'i?h'.encode('ascii')
print(s.size)
print(s.pack(17, True, 30))

print(s.unpack(b'\x00\x00\x00\x11\x01\x00\x1e\x00'))

# help(s)
# print(s.__doc__)
# for field in s.__doc__.splitlines():
#     print(field)
#

struct_type_to_class = {'i': int, 'd': float, '?': bool, 's': str}
def to_tuple(s):
    return tuple(struct_type_to_class[code](val) for code, val in s.iter_unpack(s.s))

x = to_tuple(s)
print(x)

def from_tuple(s, tpl):
    return s.pack(*tpl)

x = from_
