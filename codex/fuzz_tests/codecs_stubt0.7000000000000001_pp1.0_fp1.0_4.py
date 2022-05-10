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

def test(encoding):
    # check error handling of encoding bytes
    # will trigger a UnicodeDecodeError
    try:
        u"\xc0".encode(encoding)
    except UnicodeDecodeError as exc:
        # should be able to recover
        u"\xc0".encode(encoding, "add_one_codepoint")
        # should not be able to recover
        try:
            u"\xc0\xc0".encode(encoding, "add_one_codepoint")
        except UnicodeDecodeError as exc:
            pass
        else:
            print("unable to trigger UnicodeDecodeError")
    except:
        print("unable to trigger UnicodeDecodeError")

    # check error handling of decoding bytes
    # will trigger a UnicodeEncodeError
    try:
        u"\u0100".encode(encoding)
    except UnicodeEncodeError as exc:
        # should be able to recover
        u"\u0100".encode(encoding, "add_one_codepoint")
        # should not
