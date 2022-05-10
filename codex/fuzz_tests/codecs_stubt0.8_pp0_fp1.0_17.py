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

encoding = 'iso8859-1'

# get an encoding that is able to handle invalid bytes
try:
    codecs.getencoder(encoding)
except LookupError:
    skip_reason = 'invalid encoding'
    raise unittest.SkipTest(skip_reason)

# simple non-regression test, check that the error handler
# receives UnicodeDecodeError and not UnicodeEncodeError
with BytesIO() as f:
    f.write(b'\xFF')
    f.seek(0)
    with codecs.getreader(encoding)(f, errors='add_one_codepoint') as bz2_reader:
        bz2_reader.read()

# non-regression test for issue #26174: make sure that the callback
# is called with the correct error
with BytesIO() as f:
    f.write(b'\xFF')
    f.seek(0)
    with codecs.getreader(
        encoding.replace('iso', 'utf')
    )(f, errors='add_
