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
    import test_support
    run_unittest(TestUTF8)
    run_unittest(TestUTF8Incremental)
    run_unittest(TestLatin1)
    run_unittest(TestBOM)
    run_unittest(TestBOM_BE)
    run_unittest(TestUTF16)
    run_unittest(TestUTF16_BE)
    run_unittest(TestUTF16Ex)
    run_unittest(TestUTF32)
    run_unittest(TestUTF32_BE)
    run_unittest(TestUTF16_Surrogates)
    run_unittest(TestUTF32_Surrogates)
    run_unittest(TestErrorHandling)
    run_unittest(TestRegisterError)
    run_unittest(TestRawUnicodeEscape)
    run_unittest(TestUnicodeEscape)
    run_unittest(TestLatin1Punctuation)
    run_unittest(TestX
