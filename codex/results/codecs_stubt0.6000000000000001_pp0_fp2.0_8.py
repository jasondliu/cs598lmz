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

def test_main():
    encodings = ["utf-8", "utf-16-be", "utf-32-be"]
    for encoding in encodings:
        # Check that encode and decode round-trip.
        for test_str in ["a", "ab", "abc", "abcd"]:
            encoded = test_str.encode(encoding)
            decoded = encoded.decode(encoding)
            assert decoded == test_str

        # Check that encode errors are handled correctly.
        for test_str in ["\ud800", "\udc00"]:
            try:
                encoded = test_str.encode(encoding)
            except UnicodeEncodeError:
                pass
            else:
                raise Exception("expected UnicodeEncodeError")

        # Check that decode errors are handled correctly.
        for test_bytes in [b'\x00', b'\x00\x00', b'\x00\x00\x00']:
            try:
                decoded = test_bytes.decode(encoding)
            except UnicodeDecode
