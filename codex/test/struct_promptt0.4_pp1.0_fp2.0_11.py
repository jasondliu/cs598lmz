import _struct
# Test _struct.Struct

# The format string used for testing.
fmt = 'hhl5s'

# The expected size of the above format.
size = _struct.calcsize(fmt)

# The expected exception raised by an incorrect format.
error = TypeError

# Expected results from packing various data values.
