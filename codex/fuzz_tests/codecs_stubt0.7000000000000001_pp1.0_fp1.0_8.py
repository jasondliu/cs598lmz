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

# test codecs
def test_codecs():

    def check_codecs(encoding, errors, text, expected):
        # encode text with given errors option
        encoded = text.encode(encoding, errors)
        if encoded != expected:
            print("%s encoding: %r failed" % (encoding, errors))

        # decode bytes with given errors option
        decoded = encoded.decode(encoding, errors)
        if decoded != text:
            print("%s decoding: %r failed" % (encoding, errors))

        # test the error handler
        try:
            encoded = text.encode(encoding)
        except UnicodeEncodeError:
            # expected
            pass
        else:
            print("%s encoding: %r should have failed" % (encoding, errors))

        try:
            decoded = encoded.decode(encoding)
        except UnicodeDecodeError:
            # expected
            pass
        else:
            print("%s decoding: %r should have failed" % (encoding, errors))

    #
