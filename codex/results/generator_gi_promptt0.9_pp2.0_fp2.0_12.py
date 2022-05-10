gi = (i for i in ())
# Test gi.gi_code.co_flags, which is the __flags__ attribute
assert gi.gi_code.co_flags & 0x20  # CO_GENERATOR flag
# Check __name__, __qualname__, __text_signature__, __annotations__
assert gi.gi_code.co_name == '<genexpr>'
assert gi.gi_code.co_qualname == '<genexpr>'
assert gi.gi_code.co_firstlineno == 1
assert gi.gi_code.co_lnotab == b''
with pytest.raises(TypeError):
    gi.gi_code.co_varnames
with pytest.raises(TypeError):
    gi.gi_code.co_filename
with pytest.raises(TypeError):
    gi.gi_code.co_freevars
with pytest.raises(TypeError):
    gi.gi_code.co_consts
with pytest.raises(TypeError):
    gi.gi_code.co_cellvars
with
