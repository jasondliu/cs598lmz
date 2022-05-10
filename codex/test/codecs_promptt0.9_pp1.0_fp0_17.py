import codecs
# Test codecs.register_error()

class MyError(UnicodeError):
    pass

def bad_encode(exc):
    raise MyError("Custom error")

def bad_decode(exc):
    raise MyError("Custom error")

codecs.register_error("test.B", bad_encode)
codecs.register_error("test.D", bad_decode)

def check(errmsg, encoding, text, exception=MyError):
    msg = str(exception) + ": " + errmsg
    if sys.platform == 'darwin':
        # darwin uses "surrogateescape" by default when encoding/decoding.
        # We fix the error handler to avoid this.
        try:
            codecs.register_error("surrogateescape", bad_encode)
            codecs.register_error("surrogatepass", bad_decode)
            text = text.encode("utf-8")
        except AttributeError:
            pass
    try:
        text.encode(encoding)
    except exception:
        pass

