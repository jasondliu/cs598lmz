import _struct
# Test _struct.Struct with all standard format characters.
for format in 'xbBhHiIlLfdspP':
    s = _struct.Struct(format)
    size = s.size
    print(s)
    print(s.format, repr(s.pack(*range(size))), s.unpack(_struct.pack(format, *
        range(size))), sep='\n')
    print()
