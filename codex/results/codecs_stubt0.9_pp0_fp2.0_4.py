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

class TestReader:
    def test_encoding_errors(self):
        # tests that the right decoding errors set the right attributes
        d = codecs.lookup('iso8859-1')
        e = codecs.lookup('utf-8')
        s = b'\xf2\xf2\xf2' # invalid utf-8 is three bytes
        r = d.incrementaldecoder.range_decoder(s)
        tmp = r.read(10) # should be one '\xf2'
        assert(tmp == b'\xf2')
        assert(r.decoding_error)
        assert(r.decoding_failed)
        assert(r.decoding_buffer == b'\xf2\xf2\xf2')
        assert(r.bytes_decoded == 1)
        r.setstate(0)
        r.seek(1, 1) # seek back
        tmp = r.read(10) # now should be 1 more '\xf2'
        assert(tmp == b'\xf2')
        assert(r.
