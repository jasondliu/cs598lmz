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

# Test utf-32 BE codec
encoder = codecs.getencoder('utf-32-be')
decoder = codecs.getdecoder('utf-32-be')

for unichr in (u"\ud800", u"\udc00"):
    for replacement in ('', 'replace', 'backslashreplace', 'xmlcharrefreplace', 'add_one_codepoint'):
        print('-', unichr, replacement)
        try:
            encoder(unichr, replacement)
        except UnicodeEncodeError as exc:
            print('UnicodeEncodeError:', end=' ')
            if replacement == 'add_one_codepoint':
                print(exc.start)
                try:
                    encoder(unichr, 'add_utf32_bytes')
                except UnicodeEncodeError as exc:
                    print(exc.start)
                else:
                    print('???')
            else:
                print('???')
        except Exception as exc:
            print(type(exc), ':', exc)

