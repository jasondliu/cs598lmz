import _struct
# Test _struct.Struct.format_map() without any substitutions
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    Struct = _struct.Struct('i')
    fmt = Struct.format_map(dict())

assert [str(x.message) for x in w] == \
    ['_struct.Struct.format_map() is deprecated; use native format() instead']
assert fmt == 'i'

# Test _struct.Struct.format_map() with substitutions
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    Struct = _struct.Struct('i')
    fmt = Struct.format_map({'i': 'f', 'f': 'i'})

assert [str(x.message) for x in w] == \
    ['_struct.Struct.format_map() is deprecated; use native format() instead']
assert fmt == 'f'

# Test _struct.Struct.unpack_from() without format string
