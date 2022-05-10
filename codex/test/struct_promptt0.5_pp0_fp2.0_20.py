import _struct
# Test _struct.Struct.__new__

try:
    _struct.Struct("")
except TypeError:
    pass
else:
    raise TestFailed("expected TypeError")

try:
    _struct.Struct("", "")
except TypeError:
    pass
else:
    raise TestFailed("expected TypeError")

try:
    _struct.Struct("", "", "")
except TypeError:
    pass
else:
    raise TestFailed("expected TypeError")

try:
    _struct.Struct("", "", "", "")
except TypeError:
    pass
else:
    raise TestFailed("expected TypeError")

try:
    _struct.Struct("", "", "", "", "")
except TypeError:
    pass
else:
    raise TestFailed("expected TypeError")

try:
    _struct.Struct(1)
except TypeError:
    pass
else:
    raise TestFailed("expected TypeError")

