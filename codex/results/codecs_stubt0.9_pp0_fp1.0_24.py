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


encoding = "utf-32-be"

class TestToken(unittest.TestCase):
    def test_error_stack_overflow(self):
        # Here we check that the implementation doesn't segfault when
        # the error handler recurses too much.
        exc = None
        try:
            data = str('\xd4\x53')
            data.encode(encoding, 'add_utf16_bytes')
        except UnicodeEncodeError as e:
            self.assertIn(e.reason, ("unexpected byte", "illegal byte"))
            exc = e
        self.assertIsNot(exc, None)

        self.assertEqual(str(exc),
                             "UnicodeEncodeError: '%s' codec can't encode "
                             "character u'\\u1234' in position 0: %s"
                             %(encoding, exc.reason))

    def test_start_bytes(self):
        # Here we check that the start field of the exception has one more
        # byte than what was actually provided in the input
