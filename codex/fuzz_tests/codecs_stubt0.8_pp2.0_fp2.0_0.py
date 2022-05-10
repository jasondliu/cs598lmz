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

def test_main(verbose=None):
    # ASCII: doesn't define any fallbacks
    for encoding in ['ascii', 'iso-8859-1']:
        for errors in ['strict', 'replace', 'ignore']:
            for badencoding in ['utf-8-sig', 'utf-32', 'utf-16']:
                try:
                    badstring = u'x\xfd'.encode(badencoding)
                except UnicodeEncodeError:
                    continue
                try:
                    u = badstring.decode(badencoding).encode(encoding, errors)
                except UnicodeDecodeError:
                    continue
                if verbose:
                    print('%s -> %s, %s' % (badencoding, encoding, errors))


    # UTF-8: fallbacks to UTF-8
    for encoding in ['iso-8859-1', 'iso-8859-15']:
        for errors in ['strict', 'replace', 'ignore']:
            for badencoding in ['utf-8-sig', 'utf-32
