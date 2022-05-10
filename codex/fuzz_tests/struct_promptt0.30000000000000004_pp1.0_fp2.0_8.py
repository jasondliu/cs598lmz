import _struct
# Test _struct.Struct

# Test that the __doc__ string is useful
assert _struct.Struct.__doc__.startswith("Struct(fmt) -> compile time struct object")

# Test that the struct module can be used to create a Struct
import struct
assert isinstance(struct.Struct("i"), _struct.Struct)

# Test that the struct module can be used to create a Struct
import _struct
assert isinstance(_struct.Struct("i"), _struct.Struct)

# Test that a Struct can be created from a Struct
assert isinstance(_struct.Struct("i"), _struct.Struct)

# Test that a Struct can be created from a Struct
assert isinstance(_struct.Struct("i"), _struct.Struct)

# Test that a Struct can be created from a Struct
assert isinstance(_struct.Struct("i"), _struct.Struct)

# Test that a Struct can be created from a Struct
assert isinstance(_struct.Struct("i"), _struct.Struct)

# Test that a Struct can be created from a Struct
assert isinstance(_struct.Struct("i"), _struct.Struct)

# Test
