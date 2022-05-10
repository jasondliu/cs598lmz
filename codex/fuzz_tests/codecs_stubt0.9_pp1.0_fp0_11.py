import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

# Also test some for non-decoding errors
class WrongException(Exception):
    def __init__(self):
        self.object = None
        self.start = None
        self.end = None
        self.reason = None

class EncodingError(UnicodeError):
    def __init__(self, object, start, end, reason):
        UnicodeError.__init__(self, object, start, end, reason)

class CodingError(UnicodeError):
    def __init__(self, object, start, end, reason):
        UnicodeError.__init__(self, object, start, end, reason)

def wrong_exception(exc):
    global x
    x = exc.start
    return ("",)

def return_wrong_exception(exc):
    global x
    x = exc.start
    return WrongException()

def raise_wrong_exception(exc):
    global x
    x = exc.start
    raise WrongException()

def return_encoding_error_from_bad_decode_args
