import codecs
# Test codecs.register_error()

import encodings
import test.test_support

# Error handling function that works on unicode data.
def force_unicode(exc):
    if not isinstance(exc, UnicodeDecodeError):
        raise TypeError("don't know how to handle %r" % exc)
    return (u"<%s>" % exc.object[exc.start:exc.end], exc.end)

# Error handling function that works on bytes data.
def force_bytes(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    return ("<%s>" % exc.object[exc.start:exc.end], exc.end)

class CodecsModuleTest(unittest.TestCase):

    def test_bug_449964(self):
        # This code once raised a SystemError, because PyUnicode_FromEncodedObject
        # expected a char* and got a wchar_t*.
        codecs.escape_encode(codecs.escape_decode(
