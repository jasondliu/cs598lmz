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

def test_main(verbose=None):
    from test import test_codecs
    test_classes = [test_codecs.StreamReaderTest,
                    test_codecs.StreamWriterTest,
                    test_codecs.StreamReaderWriterTest,
                    test_codecs.IncrementalNewlineDecoderTest,
                    test_codecs.IncrementalDecoderTest,
                    test_codecs.BufferedIncrementalDecoderTest,
                    test_codecs.IncrementalEncoderTest,
                    test_codecs.BufferedIncrementalEncoderTest,
                    test_codecs.StreamRecoderTest]

    support.run_unittest(*test_classes)

    # test encodings
    test_encodings('utf-16', 'utf-8')
    test_encodings('utf-16', 'utf-8', errors='add_one_codepoint')
    test_encodings('utf-16', 'utf-8', errors='add_utf16_bytes')
    test_encodings('utf-16
