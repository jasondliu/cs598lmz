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
    # "fuzzy" encodings
    for encoding in ('ascii', 'iso8859-1', 'utf8', 'utf-7', 'uu'):
        test_string = STRING + '\x81'

        if encoding == 'uu':
            test_string = test_string.encode("ascii")
        if encoding == 'utf-7':
            input_iter = (test_string, '~')
            test_string = test_string + '~-'
        else:
            input_iter = test_string

        for errors in VALID_ERRORS:
            print("Trying codecs.encode(%s, %s, %s)" %
                  (repr(input_iter), repr(encoding), repr(errors)))

            try:
                codecs.encode(input_iter, encoding, errors)
            except UnicodeEncodeError, exc:
                traceback.print_exc()
                print("Codecs failed to encode %s with error %s" % (encoding, errors))
                print
