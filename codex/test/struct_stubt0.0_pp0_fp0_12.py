from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i').__new__(str)
except TypeError as err:
    print(err)

# __init__ adds attributes and checks name is valid
try:
    s = Struct.__new__(Struct)
    s.__init__('i')
except ValueError as err:
    print(err)

# __init__ checks that the format is valid
try:
    s = Struct.__new__(Struct)
    s.__init__('z')
except ValueError as err:
    print(err)

# __init__ accepts a compiled format
s = Struct.__new__(Struct)
s.__init__(Struct('i'))

# __init__ uses a cache for compiled formats
s = Struct.__new__(Struct)
