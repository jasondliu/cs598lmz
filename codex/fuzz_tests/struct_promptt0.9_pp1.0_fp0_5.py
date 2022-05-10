import _struct
# Test _struct.Struct, regardless of what type it has
print(type(_struct.Struct('i')))

# Create a global instance
S = _struct.Struct('i')

# Make sure it can be used for internal-only purposes
def _test_internals(marker):
    # This is not in a function, so everything depends on a global
    global binop
    binop = marker
    return binop
_test_internals(42)
assert _test_internals(24) == 42

# Make sure methods work
def _test_methods():
    assert _struct.Struct('i').size == 4
    assert S.size == 4
_test_methods()

# Make sure pack works
def _test_pack(marker):
    global binop
    binop = marker
    return _struct.pack('i', marker)
x = _test_pack(42)
assert x == b'*\x00\x00\x00'
assert _test_pack(24) == b'\x18\x00\x00\x00'

# Make sure pack_
