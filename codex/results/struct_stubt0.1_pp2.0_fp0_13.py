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

# Create new Struct object from format
Struct('i')

# Compute size of format
Struct('i').size

# Create new Struct object from format and buffer
Struct('i')(buffer=b'\x12\x34\x56\x78')

# Create new Struct object from existing Struct object
Struct('i')(s)

# Create new Struct object from format and keyword arguments
Struct('i')(i=42)

# Create new Struct object from format and keyword arguments
Struct('i')(**{'i': 42})

# Create new Struct object from format and keyword arguments
Struct('i')(**dict(i=42))

# Create new Struct object from format and keyword arguments

