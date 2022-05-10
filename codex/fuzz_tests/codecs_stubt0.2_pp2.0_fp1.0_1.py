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

# test utf-8
for enc in ('utf-8', 'utf_8', 'UTF-8', 'UTF_8'):
    for error in ('strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
        print(enc, error)
        s = b'\xff'
        try:
            s.decode(enc, error)
        except UnicodeDecodeError as e:
            print(e)

# test utf-16
for enc in ('utf-16', 'utf_16', 'UTF-16', 'UTF_16'):
    for error in ('strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
        print(enc, error)
        s = b'\xff\xff'
        try:
            s.decode(enc, error)
        except UnicodeDecodeError as e:
            print(e)

# test utf-32

