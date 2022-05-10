import codecs
# Test codecs.register_error()
class CodecsTestCase(unittest.TestCase):

    def test_register_error(self):
        self.assertRaises(TypeError, codecs.register_error,
            lambda x: x)
        self.assertRaises(TypeError, codecs.register_error, "ignore", 42)
        self.assertRaises(LookupError, codecs.register_error, "__unknown_name__", codecs.replace_errors)

        ENOENT = getattr(__import__(os.name), "ENOENT", None)
        import errno
        if ENOENT is None and hasattr(errno, "ENOENT"):
            ENOENT = errno.ENOENT
        if ENOENT is not None:
            def raise_ENOENT(exc):
                raise IOError(ENOENT, "No such file or directory")
            codecs.register_error("test.raise_IOError", raise_ENOENT)
            self.assertRaises(IOError, codecs.lookup_error("test.raise_IOError"),
