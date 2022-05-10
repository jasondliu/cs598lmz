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

# __init__ is not called
try:
    s = Struct.__new__(Struct, 'i')
    s.__init__('P')
except TypeError as err:
    print(err)

# __init__ is not called
try:
    s = Struct.__new__(Struct, 'i')
    s.__init__('P', 42)
except TypeError as err:
    print(err)

# __init__ is not called
try:
    s = Struct.__new__(Struct, 'i')
    s.__init__('P', 42, 42)
except TypeError as err:
    print(err)

# __init__ is not called

