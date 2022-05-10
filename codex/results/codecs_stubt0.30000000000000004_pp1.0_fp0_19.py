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
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for errors in ('strict', 'ignore', 'replace', 'add_one_codepoint',
                       'add_utf16_bytes', 'add_utf32_bytes'):
            print('%s %s' % (encoding, errors))
            try:
                s = '\U00010FFFF'.encode(encoding, errors)
            except UnicodeEncodeError:
                pass
            else:
                print(s)
                if encoding == 'utf-8':
                    assert s == b'\xf4\x8f\xbf\xbf'
                elif encoding == 'utf-16':
                    assert s == b'\xdb\xff\xdf\xff'
                elif encoding == 'utf-32':
                    assert s == b'\xff\xfe\x00\x00'

if __name__ == "__main__":
    test_main()
