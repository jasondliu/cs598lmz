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
    s.size
except AttributeError as err:
    print(err)

# Create with module-level convenience function
Struct('i')

# Directly create a new subclass
S = Struct.__new__(Struct, 'i')
S.__init__('i')
S.size

# Create using the subclass
S = Struct('i')
S.size

# Create using the subclass, bypassing __new__
S = type(Struct)('i')
S.size

# Create using the subclass, bypassing __new__ and __init__
