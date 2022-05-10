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
    from test import test_support
    from test.test_support import run_unittest
    from test.test_support import import_module
    from test.test_support import bigmemtest

    test_support.run_unittest(
        UTF16Test,
        UTF32Test,
        UTF8Test,
        UTF16ExTest,
        UTF32ExTest,
        UTF8ExTest,
        UTF16LETest,
        UTF16BETest,
        UTF32LETest,
        UTF32BETest,
        UTF7Test,
        UTF7ExTest,
        UTF7RoundtripTest,
        UTF8RoundtripTest,
        UTF16RoundtripTest,
        UTF32RoundtripTest,
        UTF16ExRoundtripTest,
        UTF32ExRoundtripTest,
        UTF8ExRoundtripTest,
        UTF16LERoundtripTest,
        UTF16BERoundtripTest,
        UTF32LERoundtripTest,
        UTF32BERoundtripTest,
        UTF7RoundtripExTest,
        UTF8
