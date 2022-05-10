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

def test_main():
    encodings = [ 'ascii', 'latin-1', 'iso-8859-1', 'utf-8', 'utf-16-le', 'utf-16-be', 'utf-32-le', 'utf-32-be' ]
    for encoding in encodings:
        try:
            e = codecs.getencoder(encoding)
        except LookupError:
            print("WARNING: encoding %s not supported by this codec" % repr(encoding))
            continue

        try:
            d = codecs.getdecoder(encoding)
        except LookupError:
            print("WARNING: encoding %s not supported by this codec" % repr(encoding))
            continue

        if encoding == 'ascii':
            # ascii codec cannot encode characters out of range(128)
            try:
                e("abc\x81\x82\x83")
            except UnicodeEncodeError:
                pass
            else:
                raise TestFailed("ascii codec did not raise UnicodeEncodeError")

       
