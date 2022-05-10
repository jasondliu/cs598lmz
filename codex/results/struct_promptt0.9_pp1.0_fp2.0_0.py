import _struct
# Test _struct.Struct with a format string
for endian, info in map_endian_info.items():
    for fmt in formats:
        obj = _struct.Struct(fmt.replace('@', endian))
        NUM = len(fmt)
        assert_true(hasattr(obj, 'pack'))
        if fmt[-1] == 's':
            NUM = struct.calcsize(fmt)
        assert_true(hasattr(obj, 'unpack'))
        if fmt not in 'ZP':
            # expected byte order
            byteorder = (endian == '<' or (endian == '@' and
                         sys.byteorder == 'little')) and 'little' or 'big'
            if byteorder != sys.byteorder:
                num = len(data_array1)//2 + 1
                data = data_array2[:num]
            else:
                num = len(data_array2)//2 + 1
                data = data_array1[:num]
            assert_equal(obj.size, num * NUM)
            assert_equal(
