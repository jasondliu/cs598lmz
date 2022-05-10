from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')
Struct.__new__(Struct, 'i').size

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i', 42)
except TypeError:
    print('TypeError')

# __init__ is not called
try:
    Struct.__new__(Struct, 'i', 42)
except TypeError:
    print('TypeError')

# test keyword arguments
Struct('x', new=42)

# test keyword arguments
try:
    Struct('x', new=42)
except TypeError:
    print('TypeError')
