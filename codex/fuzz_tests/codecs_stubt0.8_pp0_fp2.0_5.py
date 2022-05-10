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

def test_unicode_error_args():
    # Issue #7251
    for n in range(4):
        with pytest.raises(UnicodeDecodeError) as excinfo:
            b'\xff\xff'.decode('utf-8', 'replace')
        assert str(excinfo.value) == "byte at position 0 could not be decoded"
        with pytest.raises(UnicodeDecodeError) as excinfo:
            b'\xff\xff'.decode('utf-8', 'xmlcharrefreplace')
        assert str(excinfo.value) == "byte at position 0 could not be decoded"
        with pytest.raises(UnicodeDecodeError) as excinfo:
            b'\xff\xff'.decode('utf-8', 'add_one_codepoint')
        assert str(excinfo.value) == "failed to add codepoint at position 0"

def test_utf16_error_args():
    # Issue #8792
    for n in range(4):
        with pytest.ra
