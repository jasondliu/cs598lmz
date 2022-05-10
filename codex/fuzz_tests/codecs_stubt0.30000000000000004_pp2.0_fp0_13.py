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
            print('encoding: %s, errors: %s' % (encoding, errors))
            try:
                u = '\u3042\u3044\u3046\u3048\u304a'
                b = u.encode(encoding, errors)
                u2 = b.decode(encoding, errors)
                if u != u2:
                    raise Exception('decoded string does not match')
            except UnicodeEncodeError as e:
                print('UnicodeEncodeError: %s' % e)
            except UnicodeDecodeError as e:
                print('UnicodeDecodeError: %s' % e)

if __name__ == '__main__':
    test_main()
