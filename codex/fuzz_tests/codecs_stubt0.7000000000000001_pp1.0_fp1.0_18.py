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

for encoding in ['utf-8', 'utf-16', 'utf-32']:
    try:
        print(codecs.decode(b'\xff', encoding), end=' ')
    except UnicodeDecodeError as exc:
        print(codecs.decode(b'\xff', encoding, errors='add_one_codepoint'), end=' ')
    try:
        print(codecs.decode(b'\xff\xff', encoding), end=' ')
    except UnicodeDecodeError as exc:
        print(codecs.decode(b'\xff\xff', encoding, errors='add_utf16_bytes'), end=' ')
    try:
        print(codecs.decode(b'\xff\xff\xff\xff', encoding), end=' ')
    except UnicodeDecodeError as exc:
        print(codecs.decode(b'\xff\xff\xff\xff', encoding, errors='add_utf32_bytes'), end=' ')
    print()
