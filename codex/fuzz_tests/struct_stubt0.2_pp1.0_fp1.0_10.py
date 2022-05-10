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

# test keyword arguments
Struct('i', newarg=2)

# test keyword arguments to __new__
Struct.__new__(Struct, 'i', newarg=2)

# test keyword arguments to __init__
s = Struct.__new__(Struct)
s.__init__('i', newarg=2)

# test keyword arguments to __new__ and __init__
s = Struct.__new__(Struct, 'i', newarg=2)

# test keyword arguments to __new__ and __init__
s = Struct.__new__(Struct, format='i', newarg=2)

# test keyword arguments to __new__ and __init
