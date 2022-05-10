import ctypes
# Test ctypes.CField instances
class BAR(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int)]

class BAR_A(ctypes.Structure):
    _fields_ = [("foo_a", ctypes.c_int)]

class BAR2(ctypes.Structure):
    pass

class BAR3(ctypes.Structure):
    pass

class BAR4(ctypes.Structure):
    _fields_ = [("bar3", BAR3)]

class BAR5(ctypes.Structure):
    _fields_ = [("bar3", BAR3)]

class FOO(ctypes.Structure):
    _fields_ = [("bar", BAR),
                ("bar_a", BAR_A),
                ("bar2", BAR2),
                ("bar4", BAR4),
                ("bar5", BAR5),
                ("bar6", ctypes.c_int),
                ("bar7", ctypes.c_float)
                ]

# check that a CField is not created for the _fields_
# attribute itself
with support
