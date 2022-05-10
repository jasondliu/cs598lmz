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
