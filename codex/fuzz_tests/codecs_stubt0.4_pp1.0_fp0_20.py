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

# Test for issue #2869: UTF-32 codecs should ignore BOM
for encoding in ['utf-32', 'utf-32-be', 'utf-32-le']:
    for bom in [b'', b'\xfe\xff', b'\xff\xfe']:
        for error_handler in [None, 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes']:
            for data in [b'\x00', b'\x00\x00', b'\x00\x00\x00', b'\x00\x00\x00\x00']:
                data = bom + data
                print(encoding, error_handler, data)
                decoded = data.decode(encoding, error_handler)
                print(decoded)
                encoded = decoded.encode(encoding, error_handler)
                print(encoded)
                assert encoded == data
