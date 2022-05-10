import codecs
# Test codecs.register_error()
def custom_handler(exception):
    return u"%" + str(ord(exception.object[exception.start]))
codecs.register_error("custom_handler", custom_handler)
s = u"\u1234"
s.encode("ascii", "custom_handler")

# Test UnicodeTranslateError
def custom_translate(input):
    raise UnicodeTranslateError(input, 0, 1, "custom_handler")
codecs.register_error("custom_translate", custom_translate)
s = u"\u1234"
s.encode("ascii", "custom_translate")

# Test UnicodeDecodeError
def custom_decode(input):
    raise UnicodeDecodeError("custom_handler", input, 0, 1, "test")
codecs.register_error("custom_decode", custom_decode)
"\x80".decode("ascii", "custom_decode")

# Test UTF-16 encoding/decoding
print u"\u20ac".encode("utf
