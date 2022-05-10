from _struct import Struct
s = Struct.__new__(Struct)
print(type(s))  # > <class '_struct.Struct'>
print(dir(s))   # > ['__class__', ... ,'pack', 'pack_into', 'unpack', 'unpack_from']
print(type(Struct))  # > <class 'type'>
print(Struct.__new__)
# > <built-in method __new__ of type object at 0x7ff3911fbd20>

my_struct = Struct("i?f")
# > Traceback (most recent call last):
# >   File "<stdin>", line 1, in <module>
# > TypeError: __new__() missing 1 required positional argument: 'format'
s = my_struct.__new__(my_struct)
print(s)  # > <_struct.Struct object at 0x7fe9ecfda8b8>
# dir(s)  # > ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '
