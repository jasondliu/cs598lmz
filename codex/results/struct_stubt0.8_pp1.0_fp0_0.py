from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')

print(s.size)
print(s.pack(2, b'ab', 1.1))
print(s.unpack(b'\x02ab\xcd\xcc\xcc\xcc\xcc\x1c@'))
