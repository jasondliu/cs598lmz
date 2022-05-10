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

def test(encoding):
    print(encoding)
    # This is what we expect to happen:
    #
    # >>> codecs.decode('\xFF', encoding)
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # UnicodeDecodeError: '<encoding>' codec can't decode byte 0xff in position 0: invalid start byte
    #
    # >>> codecs.decode('\xFF', encoding, 'strict')
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # UnicodeDecodeError: '<encoding>' codec can't decode byte 0xff in position 0: invalid start byte
    #
    # >>> codecs.decode('\xFF', encoding, 'replace')
    # '�'
    #
    # >>> codecs.decode('\xFF', encoding, 'ignore')
    # ''
    #
    # >>> codecs.decode('\xFF', encoding, 'add
