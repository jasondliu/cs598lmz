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

# Test for SF bug #1096155:
# http://sourceforge.net/tracker/?func=detail&atid=355470&aid=1096155&group_id=5470
# codecs.utf_8_decode should have a second argument

for charset in ['utf-8', 'utf-16', 'utf-32']:
    for errors in ['strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes']:
        print('trying', charset, errors)
        if charset == 'utf-8':
            b = b'\x80'
        elif charset == 'utf-16':
            b = b'\xff\xfe\x80\x00'
        elif charset == 'utf-32':
            b = b'\xff\xfe\x00\x00\x80\x00\x00\x00'
        for i in [0, 1, len(b)]:
            for j in [0, 1
