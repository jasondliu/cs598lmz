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

# disable 'can't encode characters' error
# XXX code duplication
def bad_encode_surrogates(encoding):
    """Return a surrogates-failing encoding error handler."""
    def surrogates_handler(exc):
        if not isinstance(exc, UnicodeEncodeError):
            raise TypeError("don't know how to handle %r" % exc)
        if not (exc.object[exc.start].startswith("\udc") and
                exc.object[exc.start].endswith("\udc")):
            raise LookupError("only know how to handle surrogates")
        return ("?" * (exc.end - exc.start), exc.end)
    return surrogates_handler

codecs.register_error("surrogatespass3", bad_encode_surrogates)

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        self.assertRaises(TypeError, codecs.register_error, 42)

    def test_strict_errors(self):
        self
