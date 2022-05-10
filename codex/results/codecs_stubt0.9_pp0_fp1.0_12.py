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

def test_function():
    str('\xff'.encode(sys.getfilesystemencoding()), 'surrogatepass')
    str('\xff'.encode(sys.getfilesystemencoding()), 'surrogateescape')
    str('\xff'.encode(sys.getfilesystemencoding()), 'ignore')
    str('\xff'.encode(sys.getfilesystemencoding()), 'replace')
    str('\xff'.encode(sys.getfilesystemencoding()), 'add_one_codepoint')
    str('\xff'.encode(sys.getfilesystemencoding()), 'add_utf16_bytes')
    str('\xff'.encode(sys.getfilesystemencoding()), 'add_utf32_bytes')

    with AssertWarns(DeprecationWarning):
        str(b'test', 'surrogatepass')
    with AssertWarns(DeprecationWarning):
        bytes('test', 'surrogatepass')
    with AssertWarns(DeprecationWarning):
        str(
