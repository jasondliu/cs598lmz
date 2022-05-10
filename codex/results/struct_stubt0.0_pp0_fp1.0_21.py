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

# created instance can be called (__new__ is not called)
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# calling uses __new__ and then __init__
s = Struct('i')
s.pack(1)

# direct call creates a new instance
Struct('i').pack(1)

# method functions stored in class namespace
Struct.pack

# method functions have an attribute for the class
Struct.
