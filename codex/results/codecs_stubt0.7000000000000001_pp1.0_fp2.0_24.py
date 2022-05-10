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

class MyStringIO(StringIO):
    def __init__(self, *args, **kw):
        self.closed = False
        super(MyStringIO, self).__init__(*args, **kw)

    def close(self):
        self.closed = True

class CodecsModuleTest(unittest.TestCase):
    # Regression test for #1060706: the 'codecs' module should not
    # raise a SystemError when the associated C code causes a MemoryError.
    def test_memory_error(self):
        # In fact, any code that causes a MemoryError should not cause a
        # SystemError, but this is the easiest code to trigger it.  Also,
        # it's not easy to test for a MemoryError in a way that doesn't
        # cause a SystemError.
        self.assertRaises(MemoryError, codecs.escape_encode, b"a" * 1000)

    def test_open(self):
        for mode in ("r", "w", "a"):
            f = codecs.open(test_support.
