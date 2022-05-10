fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
with pytest.raises(TypeError):
    # The lambda function is not actually called
    ffi.from_buffer(fn)

# As a special case, ffi.from_buffer(cffi_type) is ok: it makes a
# buffer-view of the entire 'cffi_type'.  This helps in cases where a
# 'cffi_type' has been allocated on the heap.
with pytest.raises(TypeError):
    ffi.from_buffer(ffi.CData)
p = ffi.new('struct point *')
v = ffi.from_buffer(ffi.typeof(p))
assert v.x == 0
assert v.y == 0
v.x = 123
assert p.x == 123
p.y = 234
assert v.y == 234

a = ffi.new("int[10]")
assert len(a) == 10
for i in range(len(a)):
    a[i] = i * i
av =
