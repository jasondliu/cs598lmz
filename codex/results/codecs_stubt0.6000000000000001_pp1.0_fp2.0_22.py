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

class CodecsModuleTest(unittest.TestCase):
    def test_register_error(self):
        # codecs.register_error(errors, handler)
        # errors must be a string
        self.assertRaises(TypeError, codecs.register_error, 42, add_one_codepoint)
        # handler must be a callable
        self.assertRaises(TypeError, codecs.register_error, "add_one_codepoint", 42)

        # error handler must return a tuple of two items
        self.assertRaises(TypeError, codecs.register_error, "add_one_codepoint", lambda exc: None)
        self.assertRaises(TypeError, codecs.register_error, "add_one_codepoint", lambda exc: ("a", "b", "c"))
        # first item of the tuple must be a unicode object
        self.assertRaises(TypeError, codecs.register_error, "add_one_codepoint", lambda exc: (42, exc.start))
        # second item of the
