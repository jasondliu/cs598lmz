import codecs
# Test codecs.register_error()
def bad_error_method(exc):
    raise TypeError("bad call")
codecs.register_error("test.bad_error_method", bad_error_method)
codecs.register_error("test.bad_error_method2", bad_error_method)
def bug512345_method(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u"\ufffd", exc.start + 1)
    elif isinstance(exc, UnicodeEncodeError):
        return (u"\ufffd", exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)
codecs.register_error("test.bug512345", bug512345_method)

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)
    def decode(self, input, errors='strict'):
        return codecs.charmap_decode
