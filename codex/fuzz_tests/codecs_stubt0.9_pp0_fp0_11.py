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

def test_roundtrips():
    for input_name in _util.ALL_BYTESTRING_ENCODINGS:
        for output_name in _util.ALL_BYTESTRING_ENCODINGS:
            # The below check is needed because (for example) the
            # 'shift-jis' codec on OSX reads and writes mac japanese text
            # when the given name is 'sjis' or 'shift_jis', but full unicode
            # text when the given name is 'shift-jis'.
            if (input_name == 'shift-jis' or
                output_name == 'shift-jis'):
                if (input_name != 'shift-jis' or
                    output_name != 'shift-jis'):
                    continue
            if (input_name == 'mac_japanese' or
                output_name == 'mac_japanese'):
                if (input_name != 'mac_japanese' or
                    output_name != 'mac_japanese'):
                    continue
            if (input_
