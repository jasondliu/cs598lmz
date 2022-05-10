from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')
Struct.__new__(Struct, 'i').size

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i').__new__('s')
except TypeError:
    print('TypeError')

# __init__ is not called
try:
    s = Struct.__new__(Struct)
except TypeError:
    print('TypeError')

# __init__ must be able to initialize the instance
try:
    Struct.__new__(Struct, 'i', 'j').size
except TypeError:
    print('TypeError')

# __init__ is not called
try:
    s = Struct.__new__(Struct)
    s.__init__('i')
except TypeError:
    print('TypeError')

# __init__ is not called
