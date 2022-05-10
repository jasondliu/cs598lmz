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

class TestDecode(unittest.TestCase):
    def test_decode_errors(self):
        # Test the various error handling schemes
        #
        # XXX: the error handling schemes are not tested in a very
        # thorough way.  It would be nice to have more tests.
        #
        # XXX: the error handling schemes are not tested for
        # encodings which have a state.
        #
        # XXX: the error handling schemes are not tested for
        # encodings which have a state, and for which the decoder
        # returns an invalid continuation byte.
        #
        # XXX: the error handling schemes are not tested for
        # encodings which have a state, and for which the decoder
        # returns an invalid continuation byte, and for which the
        # call to the decoder is not the first call in a stream.
        #
        # XXX: the error handling schemes are not tested for
        # encodings which have a state, and for which the decoder
        # returns an invalid byte.
        #
        # XXX: the error handling schemes are
