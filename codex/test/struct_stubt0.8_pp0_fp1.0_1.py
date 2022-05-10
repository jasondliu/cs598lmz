from _struct import Struct
s = Struct.__new__(Struct)
print(s)
# <_struct.Struct object at 0x0000023C2B01E2A0>

s.__init__('l')

try:
    s.pack(1)
except AttributeError as e:
    print(e)
# pack requires exactly '1' arguments

try:
    s.pack(1, 2)
except TypeError as e:
    print(e)
# pack takes at most '1' arguments

assert s.pack(1) == b'\x00\x00\x00\x00\x00\x00\x00\x01'
assert s.pack(-1) == b'\xff\xff\xff\xff\xff\xff\xff\xff'

s = Struct('ff')
assert s.unpack(b'\x00\x00\x00\x00\x00\x00\x00\x00' * 2) == (0, 0)
