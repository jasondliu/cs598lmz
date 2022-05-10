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


# check illegal codepoints
def check_exception(self, s, exc_type, start=0, end=None, enc_start=0, exc_msg=None, encoding='ascii'):
    enc_s = s.encode(encoding)
    if exc_type is None:
        for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint'):
            encoded = enc_s.decode(encoding, errors)
            self.assertEqual(encoded, s, "Error with {} while decoding {} using {}".format(errors, repr(enc_s), encoding))

            if errors == "strict":
                # On Python 3, all byte string arguments to
                # str()/unicode() are considered binary data. So even though
                # we are passing str() with the 'ascii' encoding and
                # 'strict' buffer decoding (which should fail), the
                # str(b'1234') gets converted to 4 separate characters
                # '1', '2', '3' and '4'. This is what
