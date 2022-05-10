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

#
#  Tests
#

def test_main():
    unicode_test_strings = ['a'*i for i in range(1, 100)]
    for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32']:
        print('testing encoding:', encoding)
        for input in unicode_test_strings:
            # Encode as bytes
            try:
                encoded = input.encode(encoding)
            except UnicodeEncodeError:
                print('UnicodeEncodeError', input, encoding)
                continue
            # Decode with 'strict'
            try:
                decoded = encoded.decode(encoding)
            except UnicodeDecodeError:
                print('UnicodeDecodeError', encoded, encoding)
                continue
            assert decoded == input
            # Decode with 'replace'
            try:
                decoded = encoded.decode(encoding, 'replace')
            except UnicodeDecodeError:
                print('UnicodeDecodeError', encoded, encoding)

