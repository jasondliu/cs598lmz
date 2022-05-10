from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__ is Struct

# __init__ is a plain instance method
Struct.__init__ is s.__init__

# __init__ always returns None
s.__init__('i') is None

# calling the class is the same as calling __new__ followed by __init__
Struct('i').__init__('i') is None
Struct('i') is Struct.__new__(Struct, 'i')

# calling the instance is the same as calling __init__
s('i') is None
s.__init__('i') is None

# calling the instance with other arguments is an error
try:
    s(1, 2)
except TypeError:
    print('TypeError')

# calling the class with other arguments after the format
# results in a TypeError
try:
    Struct('i', 1, 2)
except TypeError:
    print('TypeError')

# calling the class with other arguments before the format
# results
