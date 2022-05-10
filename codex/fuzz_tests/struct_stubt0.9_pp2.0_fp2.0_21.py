from _struct import Struct
s = Struct.__new__(Struct)

try:
    s.__init__(b'=i') # double-freed
    assert False
except RuntimeError:
    pass

try:
    s.__init__(b'=i') # invalid nextsize size
    assert False
except RuntimeError:
    pass

try:
    s.__init__(b'=i') # invalid nextsize address
    assert False
except RuntimeError:
    pass
