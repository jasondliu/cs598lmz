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

def test_input_codecs(codec):
    errorhandler = codecs.lookup_error("add_one_codepoint")
    # Test input codecs
    test_string = codec + "a"
    test_string_bytes = test_string.encode(codec)
    for i in range(len(test_string)):
        test_string_bytes_copy = test_string_bytes[:]
        del test_string_bytes_copy[i]
        test_string_decode = test_string_bytes_copy.decode(codec, errors="add_one_codepoint")
        if test_string_decode[i] != "a":
            print(codec, "at position", i, "failed")
            print(test_string_decode)
            print(test_string_decode[i])
            print(repr(test_string_decode))
            print(repr(test_string_decode[i]))
            assert 0

def test_output_codecs(codec):
   
