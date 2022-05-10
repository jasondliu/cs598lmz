from _struct import Struct
s = Struct.__new__(Struct)
print(list(s.__dict__.keys()))
# ['__module__',
#  '__doc__',
#  'format',
#  '__init__',
#  '__new__',
#  '__getitem__',
#  'size',
#  'pack',
#  'unpack',
#  'unpack_from',
#  'iter_unpack']
print(s.iter_unpack)
# <method 'iter_unpack' of 'Struct' objects>
s.__init__(s, 'I 2s f')
print(s.iter_unpack)
# <bound method Struct.iter_unpack of Struct('I 2s f')>
print(list(s.iter_unpack(b'\x12\x34\x56\x78spam')))
# [(4660, b'sp', 0.0)]
