import ctypes
# Test ctypes.CField structure
cfield_test = ctypes.CField(
    ctypes.c_int,
    'test',
    ctypes.c_void_p,
    ctypes.c_void_p,
    None,
    None,
    0,
    0,
    0,
    0,
    0,
    None
)
assert cfield_test.value == ctypes.c_int
assert cfield_test.name == 'test'
assert cfield_test.offset == ctypes.c_void_p
assert cfield_test.size == ctypes.c_void_p
assert cfield_test.alignment == None
assert cfield_test.bitsize == 0
assert cfield_test.bitoffset == 0
assert cfield_test.type_index == 0
assert cfield_test.flags == 0
assert cfield_test.flags_enum == 0
assert cfield_test.type_index == 0
assert cfield_test.type_index == 0
assert cfield_test.type_index == 0
assert cfield_test.type_index
