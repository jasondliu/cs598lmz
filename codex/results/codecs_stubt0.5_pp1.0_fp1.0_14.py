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

with open('utf16.txt', 'rb') as f:
    utf16 = f.read()

with open('utf32.txt', 'rb') as f:
    utf32 = f.read()

def test_utf16_surrogates(utf16=utf16):
    with pytest.raises(UnicodeDecodeError) as excinfo:
        utf16.decode('utf-16')
    assert excinfo.value.reason == 'surrogates not allowed'
    assert utf16.decode('utf-16', 'add_one_codepoint') == '\udc00a'
    assert utf16.decode('utf-16', 'replace') == '\ufffd\ufffd'
    assert utf16.decode('utf-16', 'ignore') == ''
    with pytest.raises(UnicodeDecodeError) as excinfo:
        utf16.decode('utf-16', 'add_utf16_bytes')
    assert excinfo.value.reason == 'surrogates not allowed'

