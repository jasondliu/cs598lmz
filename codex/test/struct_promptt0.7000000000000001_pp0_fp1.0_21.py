import _struct
# Test _struct.Struct instances.

# _struct.Struct() should not be callable.

try:
    w = _struct.Struct()
except TypeError:
    pass
