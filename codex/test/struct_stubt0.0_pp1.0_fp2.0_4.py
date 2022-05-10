from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i', 42)
except TypeError:
    pass

# __init__ now takes an additional argument
try:
    s.__init__('i')
except TypeError:
    pass

# __init__ now returns None
r = s.__init__('i')
r is None

# calling __init__ twice is OK
s.__init__('i')

# calling __init__ with a bad format no longer raises TypeError
try:
    s.__init__('z')
except error:
    pass

# calling __init__ with a bad format now leaves the instance unchanged
s.format == 'i'

# calling __init__ with a bad format now leaves the size unchanged
s.size == 4

# calling __init__ with a bad format now leaves the format unchanged
