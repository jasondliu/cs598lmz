import _struct
# Test _struct.Struct

# Test all the different sized patterns

for fmt in 'xcbBhHiIlLqQfd':
    # check automatic cache
    s = _struct.Struct(fmt)
    s = _struct.Struct(fmt)
    # create some data and encode it
    data = 1/7., -2**32
    encoded = s.pack(*data)

    # test decoding
    result = s.unpack(encoded)
    assert result == data, `result`

# now set the cache size to 5 and test that it works
old_cache_size = _struct.STRUCT_PARAMS["cache_size"]
_struct.STRUCT_PARAMS["cache_size"] = 5

# populate the cache
for fmt in (
    'cbBhHiIlLqQfd',
    'xcbBhHiIlLqQfd',
    '0xcbfBhHiIlLqQfd',
):
    s = _struct.Struct(fmt)

# This should cause the oldest entry in the cache to be thrown away
s = _struct.Struct('b10
