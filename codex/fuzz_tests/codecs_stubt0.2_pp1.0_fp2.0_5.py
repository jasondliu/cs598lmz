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
    # Test UTF-16 and UTF-32 codecs
    for encoding in ('utf-16', 'utf-32'):
        # Test decoding
        for error in ('strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
            for byteorder in ('little', 'big'):
                for byteorderchar in ('<', '>'):
                    for bom in (True, False):
                        for data in (b'\xff', b'\xff\xff', b'\xff\xff\xff', b'\xff\xff\xff\xff'):
                            if bom:
                                data = byteorderchar.encode() + data
                            if encoding == 'utf-16':
                                data = data[:-2]
                            elif encoding == 'utf-32':
                                data = data[:-4]
                            if byteorder == 'little':
                                data = data[::-1]
                            data = data.decode(encoding,
