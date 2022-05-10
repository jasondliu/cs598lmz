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
    import test.test_support

    test.test_support.run_unittest(CodecTest)
    test.test_support.run_unittest(StreamReaderTest)
    test.test_support.run_unittest(StreamWriterTest)
    test.test_support.run_unittest(IncrementalEncoderTest)
    test.test_support.run_unittest(IncrementalDecoderTest)
    test.test_support.run_unittest(BufferedIncrementalDecoderTest)
    test.test_support.run_unittest(BufferedReaderTest)
    test.test_support.run_unittest(BufferedWriterTest)
    test.test_support.run_unittest(UTF8Test)
    test.test_support.run_unittest(UnicodeTranslateTest)
    test.test_support.run_unittest(RegisterErrorTest)
    test.test_support.run_unittest(OpenTest)
    test.test_support.run_unitt
