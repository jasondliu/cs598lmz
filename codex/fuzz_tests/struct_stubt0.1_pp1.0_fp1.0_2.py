from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i').__new__(str)
except TypeError:
    print('TypeError')

# Issue #17230: _struct.Struct.__new__() should not accept keyword arguments
try:
    Struct.__new__(Struct, 'i', newarg=123)
except TypeError:
    print('TypeError')

# Issue #17230: _struct.Struct.__new__() should not accept keyword arguments
try:
    Struct.__new__(Struct, format='i', newarg=123)
except TypeError:
    print('TypeError')

# Issue #17230: _struct.Struct.__new__() should not accept keyword arguments
try:
    Struct.__new__(Struct, format='i', newarg=123)
except TypeError:
    print('TypeError')
