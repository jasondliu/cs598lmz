import _struct
# Test _struct.Struct
try:
    _struct.Struct("123")
except ValueError:
    pass
else:
    raise TestFailed("_struct.Struct(123) should have failed")

try:
    _struct.Struct("bj")
except ValueError:
    pass
else:
    raise TestFailed("_struct.Struct('bj') should have failed")

try:
    _struct.Struct("=*")
except ValueError:
    pass
else:
    raise TestFailed("_struct.Struct('=*') should have failed")

try:
    _struct.Struct("123")
except ValueError:
    pass
else:
    raise TestFailed("_struct.Struct('123') should have failed")

# Test .format
try:
    _struct.Struct("123").format
except AttributeError:
    pass
else:
    raise TestFailed("_struct.Struct('123').format should fail")

try:
    _struct.Struct("b").format
except AttributeError:
    pass
else:
    raise TestFailed("_struct.Struct('
