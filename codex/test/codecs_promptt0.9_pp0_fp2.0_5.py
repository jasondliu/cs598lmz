import codecs
# Test codecs.register_error for "ignore" and "replace"


class Test_register_error:

    def test_ignore(self):
        codecs.register_error("ignore", lambda exc: ("", exc.start + 1))
        self.assertEqual(b"abc".decode("ascii", "ignore"), u"abc")
        self.assertEqual(b"abc\xffdef".decode("ascii", "ignore"), u"abcdef")
        codecs.register_error("ignore", lambda exc: ("?", exc.start + 1))
        self.assertEqual(b"abc\xffdef".decode("ascii", "ignore"), u"abc?def")
        self.assertRaises(TypeError, codecs.register_error, "ignore", None)
        self.assertRaises(TypeError, codecs.register_error, 1)

    def test_ignore_utf8(self):
        codecs.register_error("ignore", lambda exc: ("", exc.start + 1))
