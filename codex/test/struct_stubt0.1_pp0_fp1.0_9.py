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

# creating an instance calls __new__ and __init__
s = Struct('i')
s.size

# method named from the format
s.pack(1)

# format is available as an attribute
s.format

# computed attribute
s.format_code == 'i'

# other methods
s.pack_into(bytes(4), 0, 1)
s.unpack(b'\x01\x00\x00\x00')
