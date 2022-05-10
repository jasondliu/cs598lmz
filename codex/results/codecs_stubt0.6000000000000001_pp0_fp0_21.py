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
    test_support.run_unittest(TestBase64)
    test_support.run_unittest(TestUTF7)
    test_support.run_unittest(TestUTF8)
    test_support.run_unittest(TestUTF16)
    test_support.run_unittest(TestUTF32)
    test_support.run_unittest(TestUnicode)
    test_support.run_unittest(TestErrors)
    test_support.run_unittest(TestRegisterError)

if __name__ == "__main__":
    test_main()
