import codecs
# Test codecs.register_error()
import _testcapi

class UnstrippableError(UnicodeError):
    def __init__(self, obj, start, end, reason):
        self.obj = obj
        self.start = start
        self.end = end
        self.reason = reason

def unstrippable(exc):
    if not isinstance(exc, UnicodeError):
        return exc
    newexc = UnstrippableError(exc.object, exc.start, exc.end, exc.reason)
    newexc.__cause__ = exc
    return newexc

class StripTest(unittest.TestCase):

    def test_register_error(self):

        # Before registering the error handler
        self.assertRaises(UnicodeEncodeError, "\u3042".encode, "ascii", "strict")

        codecs.register_error("test.unstrippablehandler", unstrippable)
        try:
            # After registering the error handler
            self.assertRaises(UnstrippableError, "\u3042".encode, "asci
