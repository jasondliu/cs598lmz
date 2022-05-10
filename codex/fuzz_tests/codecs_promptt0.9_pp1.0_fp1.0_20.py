import codecs
# Test codecs.register_error() function

def py_error(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeDecodeError)):
        return (u'replace', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)


class TestUnicode:
    def test_register_error(self):
        # this is a test for #6275
        codecs.register_error("strict", py_error)
        codecs.register_error("replace", py_error)
        codecs.register_error("ignore", py_error)
        codecs.register_error("backslashreplace", py_error)

class TestStr:
    def test_register_error(self):
        # this is a test for #6275
        codecs.register_error("strict", py_error)
        codecs.register_error("replace", py_error)
        codecs.register_error("ignore", py_error)
        codecs.register_error("backslashreplace", py_error)


