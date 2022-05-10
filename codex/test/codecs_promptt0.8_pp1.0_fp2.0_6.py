import codecs
# Test codecs.register_error
class Internal_Test:
    def __init__(self, errors="strict"):
        self.errors = errors
    def handle_error(self, error):
        if self.errors == "strict":
            raise error
        elif isinstance(self.errors, str):
            return (self.errors, error.start + 1)
        elif hasattr(self.errors, "__call__"):
            return self.errors(error)
        raise TypeError("bad error parameter")
codecs.register_error("test.internal", Internal_Test)

# It's not possible to test the codec error callback mechanism directly
# since the test script would exit with a traceback.
# So we test the callback mechanism indirectly by trying
# to encode/decode data using non-existing codecs or codecs
# with non-existing error handlers.

# Encode an Unicode object using a non-existing codec to trigger an error.
try:
    u"\u3042".encode("nonexisting")
except LookupError:
    pass
