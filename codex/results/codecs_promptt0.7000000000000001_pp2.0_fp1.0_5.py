import codecs
# Test codecs.register_error
import re

if __name__ == "__main__":
    # Test custom encoders
    assert codecs.encode("abc\u1234\u20ac\u8000", "test.test_codecs.test_encodings.test_codec") == "abc\x04\x12\xe2\x82\xac\x01\x00"
    assert codecs.encode("abc\u1234\u20ac\u8000", "test.test_codecs.test_encodings.test_incrementalencoder") == "abc\x04\x12\xe2\x82\xac\x01\x00"
    assert codecs.encode("abc\u1234\u20ac\u8000", "test.test_codecs.test_encodings.test_streamreaderwriter") == "abc\x04\x12\xe2\x82\xac\x01\x00"
    # Test custom decoders
    assert codecs.decode("abc\x04\x12\xe2\
