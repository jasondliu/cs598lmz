import ctypes
# Test ctypes.CField structure
p = setup_ctypes_test()
print_ctypes_field(p, "c_bool")
print_ctypes_field(p, "c_byte")
print_ctypes_field(p, "c_char")
print_ctypes_field(p, "c_char_p")
print_ctypes_field(p, "c_double")
print_ctypes_field(p, "c_float")
print_ctypes_field(p, "c_void_p")
# Are essential types different?
assert not ctypes.c_int().from_address(3193984) == \
       ctypes.c_int().from_address(3193984)
assert not ctypes.c_long().from_address(3193984) == \
       ctypes.c_long().from_address(3193984)
assert not ctypes.c_short().from_address(8293984) == \
       ctypes.c_short().from_address(8293984)
assert not ctypes.c_char().from_address(47939
