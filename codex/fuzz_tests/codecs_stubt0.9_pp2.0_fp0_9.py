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

try:
    unicode
except NameError:
    unicode = str

class StreamWriterTest(unittest.TestCase):

    def test_streamwriter(self):

        payload = 'test payload'
        reader = codecs.getreader('utf-16-be')
        writer = codecs.getwriter('utf-16-be')
        r = reader(io.BytesIO(payload.encode('utf-16-be')))
        w = writer(io.BytesIO())
        for char in r.read():
            w.write(char)
        w.seek(0)
        self.assertEqual(payload.encode('utf-16-be'), w.read())

        # this time with an incremental decoder
        r = codecs.getreader('utf-16-be')(io.BytesIO(payload.encode('utf-16-be')))
        w = codecs.getwriter('utf-16-be')(io.BytesIO())
        for char in r.read():
            w.write(char)
        w.
