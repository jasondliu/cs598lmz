import _struct
# Test _struct.Struct with the native byte order:
native_test_cases = [('@i', 0x01020304, [1, 2, 3, 4]),
    ('@I', 0x04030201, [4, 3, 2, 1]),
    ('@h', 0x0102, [1, 2]),
    ('@H', 0x0201, [2, 1]),
    ('@b', 0x01, [1]),
    ('@B', 0xff, [255])]
for format_char, value, expected in native_test_cases:
    for format_string in [format_char, '!' + format_char, '>' + format_char,
        '<' + format_char]:
        s = _struct.Struct(format_string)
        actual = list(s.pack(value))
        assert actual == expected, '%r.pack(%r) == %r != %r' % (s.format, value,
            actual, expected)
        actual = s.unpack(bytes(actual))[0]
