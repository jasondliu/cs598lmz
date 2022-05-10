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

class MyUnicodeError(UnicodeError):
    def __init__(self, *args):
        pass

def raise_unicode_error(exc):
    if isinstance(exc, UnicodeEncodeError):
        raise MyUnicodeError
    return ("a", exc.start)

codecs.register_error("raise_unicode_error", raise_unicode_error)

class Test_register_error(unittest.TestCase):

    def test_register_error_functions(self):
        for encoding in ('latin-1', 'utf-16', 'utf-32'):
            for errors in ('strict', 'replace', 'ignore', 'xmlcharrefreplace',
                           'backslashreplace', 'namereplace',
                           "add_one_codepoint",
                           "raise_unicode_error"):
                try:
                    '\uDC80'.encode(encoding, errors=errors)
                except UnicodeEncodeError:
                    pass
                except UnicodeDecodeError:
                    pass
                except MyUn
