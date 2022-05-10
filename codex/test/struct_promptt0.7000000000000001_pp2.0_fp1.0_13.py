import _struct
# Test _struct.Struct with non-native endianness.
_struct.Struct("<i").unpack(b"\x01\x02\x03\x04")
# Test _struct.Struct with non-native endianness and non-native size.
_struct.Struct("=l").unpack(b"\x01\x02\x03\x04")

# Test that the _struct module is available (bpo-27164).
assert hasattr(sys, "_struct_posix")
assert hasattr(sys, "_struct_nt")
assert hasattr(sys, "_struct_generic")
assert hasattr(sys, "_struct")

# Test that the _struct module is not available on Windows
# (bpo-27164).
assert not hasattr(sys, "_struct_nt")

# Test that the _struct module is not available on Solaris
# (bpo-27164).
assert not hasattr(sys, "_struct_posix")

# Test that the _struct module is not available on macOS
# (bpo-27164).
