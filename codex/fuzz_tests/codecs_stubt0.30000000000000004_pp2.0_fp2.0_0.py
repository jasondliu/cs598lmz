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
    # Test the error callback mechanism
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        for error_handler in ('strict', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
            if error_handler == 'add_utf16_bytes' and encoding != 'utf-16':
                continue
            if error_handler == 'add_utf32_bytes' and encoding != 'utf-32':
                continue
            print(encoding, error_handler)
            if encoding == 'utf-8':
                s = b'\xff'
            elif encoding == 'utf-16':
                s = b'\xff\xff'
            elif encoding == 'utf-32':
                s = b'\xff\xff\xff\xff'
            try:
                s.decode(encoding, error_handler)
            except UnicodeDecodeError:
                pass

if __name__ == "__main__":
    test_main
