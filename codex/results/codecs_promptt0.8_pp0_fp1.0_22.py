import codecs
# Test codecs.register_error()
# (text, encodings, errors, expected)
TESTDATA = [
    ('', 'ascii', 'strict', b''),
    ('', 'ascii', 'ignore', b''),
    ('', 'ascii', 'replace', b''),
    ('', 'ascii', 'xmlcharrefreplace', b''),
    ('', 'ascii', 'backslashreplace', b''),
    ('', 'ascii', 'namereplace', b''),
    ('', 'ascii', 'surrogateescape', b''),
    ('', 'ascii', 'surrogatepass', b''),
    ('', 'ascii', 'strict', b''),
    ('\x80', 'ascii', 'strict', None),
    ('\x80', 'ascii', 'ignore', b''),
    ('\x80', 'ascii', 'replace', b'?'),
    ('\x80', 'ascii', 'xmlcharrefreplace', b'&#128;'),
    ('\x
