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
    # test UTF-16 and UTF-32 codecs
    for encoding in ('utf-16', 'utf-32'):
        for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint',
                       'add_utf16_bytes', 'add_utf32_bytes'):
            for bom in (True, False):
                for byteorder in (-1, 0, 1):
                    print(encoding, errors, bom, byteorder)
                    if encoding == 'utf-16':
                        if bom:
                            if byteorder == -1:
                                data = b'\xff\xfe\x00\x00'
                            elif byteorder == 0:
                                data = b'\xfe\xff\x00\x00'
                            else:
                                data = b'\x00\x00\xfe\xff'
                        else:
                            if byteorder == -1:
                                data = b'\x00\x00'
                            elif byteorder == 0:
                                data
