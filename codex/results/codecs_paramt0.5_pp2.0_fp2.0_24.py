import codecs
codecs.register_error("mixed", MixedUnicodeError)
del codecs

class MixedUnicodeError(UnicodeDecodeError):
    def __init__(self, obj, *args):
        self.obj = obj
        UnicodeDecodeError.__init__(self, *args)

    def __str__(self):
        original = UnicodeDecodeError.__str__(self)
        return '%s. You passed in %r (%s)' % (original, self.obj,
                                              type(self.obj))

class BadStatusLine(Exception):
    """Raised if a server responds with a HTTP status code we don't understand."""
    def __init__(self, line):
        self.line = line
        self.args = (line,)

class HTTPConnection(httplib.HTTPConnection):
    "This class allows communication via SSL."
    default_port = HTTPS_PORT
    response_class = HTTPResponse

    def __init__(self, host, port=None, strict=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
