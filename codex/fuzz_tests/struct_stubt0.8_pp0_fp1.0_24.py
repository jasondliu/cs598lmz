from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(dict(format='>i2sh', size=8, pack=Struct.pack, unpack=Struct.unpack))
print(s.size)
print(s.pack(b'\x12\x34\x56\x78\x9a\xbc'))
print(s.unpack(b'\x12\x34\x56\x78\x9a\xbc'))

print('#' * 52 + '  Here is the class definition for `struct`:')
print(Struct.__dict__.items())
print('#' * 52 + '  Here are instance attributes for a `struct`:')
print(s.__dict__.items())

print('#' * 52 + '  Here are the defaults:')

struct_defaults = dict(format='', size=0, pack=None, unpack=None)
print(struct_defaults)
print('#' * 52 + '  Here are the attributes the user can set:')
format_field_template = '{}={:#x}'

