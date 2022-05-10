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

# _clearcache is a static method
Struct._clearcache()

# test keyword arguments
Struct('i', new=1, byteorder='big')

# test keyword arguments to __new__
Struct.__new__(Struct, 'i', new=1, byteorder='big')

# test keyword arguments to __init__
s = Struct.__new__(Struct)
s.__init__('i', new=1, byteorder='big')

# test incorrect arguments to __new__
try:
    Struct.__new__()
except TypeError:
    print('TypeError')

try:
    Struct.__new__(42
