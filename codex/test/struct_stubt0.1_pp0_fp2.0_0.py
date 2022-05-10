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

# Issue #17230: __new__ must not be a static method
try:
    Struct.__new__('i')
except TypeError:
    print('TypeError')

# Issue #17230: __new__ must be present
try:
    class S(Struct):
        pass
except TypeError:
    print('TypeError')

# Issue #17230: __new__ must accept the right arguments
try:
    class S(Struct):
        def __new__(self):
            pass
except TypeError:
    print('TypeError')

# Issue #17230: __new__ must return an instance of cls
