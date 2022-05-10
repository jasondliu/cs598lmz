import _struct
# Test _struct.Struct class.

f = _struct.Struct("i")

# test __doc__
assert f.__doc__ == "compiled struct object"

# test __new__
assert f.__new__(f, "i") is f

# test invalid format
try:
    _struct.Struct("z")
except ValueError:
    pass
