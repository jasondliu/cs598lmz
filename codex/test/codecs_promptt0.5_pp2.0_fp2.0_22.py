import codecs
# Test codecs.register_error(), bug #1457894.
import codecs

def bad_decode(input, errors):
    raise UnicodeDecodeError(
        'test', input, 0, len(input), 'test error message')

codecs.register_error('test', bad_decode)

class Test_UnicodeEncodeError:

    def test_init(self):
        # calling UnicodeEncodeError with bad parameters
        raises(TypeError, UnicodeEncodeError)
        raises(TypeError, UnicodeEncodeError, "")
        raises(TypeError, UnicodeEncodeError, "", b"", 0, 10, "")
        raises(TypeError, UnicodeEncodeError, "", b"", 0, 10, "", b"")
        raises(TypeError, UnicodeEncodeError, "", b"", 0, 10, "", b"", None)

        u = UnicodeEncodeError("utf-8", b"", 0, 1, "ouch")
        assert u.encoding == "utf-8"
        assert u.object == b""
        assert u.start == 0
