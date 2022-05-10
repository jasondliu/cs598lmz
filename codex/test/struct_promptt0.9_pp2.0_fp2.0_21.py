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
