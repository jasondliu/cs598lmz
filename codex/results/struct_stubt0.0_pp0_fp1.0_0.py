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
    s.__init__()
except TypeError:
    pass

# __init__ now returns None
r = s.__init__('i')
r is None

# calling __init__ twice is an error
try:
    s.__init__('i')
except TypeError:
    pass

# test __repr__
repr(s)

# can't create instances without calling __init__
try:
    Struct.__new__(Struct)
except TypeError:
    pass

# test __reduce__
import pickle
pickle.loads(pickle.dumps(s))

# test __sizeof__
import sys
if hasattr(
