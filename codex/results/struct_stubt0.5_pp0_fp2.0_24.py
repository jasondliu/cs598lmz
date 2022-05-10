from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'hi32s'
s.size = calcsize(s.format)
print(s.size)
print(s.format)

#反结构
print(unpack(s.format, b'\x12\x34\x56\x78'))

#结构化类型
class Structure:
    _fields_ = [
        ('<i', 'tag'),
        ('i', 'data')
    ]

class NestedStructure:
    _fields_ = [
        ('<i', 'tag'),
        ('(ii)', 'data')
    ]

print(Structure.__new__(Structure, 1, 2))
print(NestedStructure.__new__(NestedStructure, 1, (2, 3)))

#结构化类型的特殊属性
#__slots__
class Point(Structure):
    _fields_ = [
        ('<d',
