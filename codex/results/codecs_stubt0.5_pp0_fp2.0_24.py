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
    from test.test_support import run_unittest, import_module
    test_support = import_module('test.test_support')
    from test.script_helper import assert_python_ok

    # Test that the surrogatepass handler works for wide builds
    # (see issue #4367).
    run_unittest(ErrorHandlingTestCase)

    # Test that the surrogatepass handler works for narrow builds
    # (see issue #4367).
    assert_python_ok('-Wi', '-c',
                     'import sys; sys.exit(int(sys.maxunicode < 0xffff))')

if __name__ == '__main__':
    test_main()
