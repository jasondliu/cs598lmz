import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

def dump_list(list, file=sys.stdout):
    for i, item in enumerate(list):
        print("{}:".format(i), end=' ', file=file)
        if isinstance(item, str):
            file.write("'")
            file.write(item)
            file.write("' ")
        else:
            file.write(repr(item))
            file.write(" ")
    file.write("\n")

def assert_convert_equal(encode, decode, expect_encode, expect_decode,
                         encode_kwargs={}, decode_kwargs={}):
    r = codecs.charmap_encode(encode, expect_decode, **encode_kwargs)
    r = bytes(r[0])
    assert r == expect_encode

    r = codecs.charmap_decode(decode, expect_encode, **decode_kwargs)
    r = str(r[0])
    assert r == expect_decode

def test_dec
