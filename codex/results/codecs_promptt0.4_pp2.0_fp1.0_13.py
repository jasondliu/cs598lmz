import codecs
# Test codecs.register_error
import encodings.utf_8

def test_main():
    # Test codecs.register_error
    def bad_decode(input, errors='strict'):
        raise UnicodeDecodeError("bad", input, 0, 1, "bad")
    def bad_encode(input, errors='strict'):
        raise UnicodeEncodeError("bad", input, 0, 1, "bad")
    codecs.register_error("test.bad_decode", bad_decode)
    codecs.register_error("test.bad_encode", bad_encode)
    for encoding in ("utf-8", "utf-16", "utf-32", "utf-16-le", "utf-16-be",
                     "utf-32-le", "utf-32-be", "unicode-internal"):
        try:
            unicode("abc", encoding, "test.bad_decode")
        except UnicodeDecodeError, exc:
            assert exc.reason == "bad"
        try:
            u"abc".encode(encoding, "test.
