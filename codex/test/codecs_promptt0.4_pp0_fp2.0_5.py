import codecs
# Test codecs.register_error()
def test_register_error():
    def handler(exc):
        if isinstance(exc, UnicodeDecodeError):
            x, y = exc.object[exc.start:exc.end], exc.reason
