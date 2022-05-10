import codecs
# Test codecs.register_error
class MyError(Exception):
    def __init__(self, encoding, msg):
        self.encoding = encoding
        self.msg = msg
    def __str__(self):
        return "MyError(%r, %r)" % (self.encoding, self.msg)

def my_error_handler(exc):
    if isinstance(exc, MyError):
        print("my_error_handler: %s" % exc)
        return (u"", exc.msg)
    else:
        return codecs.strict_errors(exc)

codecs.register_error("test.myerrorhandler", my_error_handler)

encoder = codecs.getencoder("ascii")
