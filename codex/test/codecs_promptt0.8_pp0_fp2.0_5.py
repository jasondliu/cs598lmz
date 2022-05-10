import codecs
# Test codecs.register_error for the ignore attribute of error handlers

def check_ignore(c):
    if c == 'x':
        return None
    assert len(c) == 1
    assert ord(c) >= 256
    return chr(ord(c)-256)


class TestIgnore:

    def test_invalid(self):
        f = codecs.getreader('ascii')(codecs.BytesIO(b'fo\x80bar'))
        g = f.read()
        assert g == 'fo\ufffdbar'
        h = f.read()
        assert h == ''

    def test_register_error(self):
        codecs.register_error('test.ignore', check_ignore)
        u = codecs.decode('fo\x80bar', 'ascii', 'test.ignore')
        assert u == 'foxbar'

    def test_lookup_error(self):
        codecs.register_error('test.ignore', check_ignore)
