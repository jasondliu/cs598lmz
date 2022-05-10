import codecs
# Test codecs.register_error() by encoding a Unicode string
# that uses a character not available in the target encoding.
# This should raise a UnicodeEncodeError.

def custom_handler(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u"\ufffd", exc.end)
    else:
        raise exc

def custom_handler_2(exc):
    if isinstance(exc, UnicodeEncodeError):
        return (u"\u1234\u5678", exc.end+1)
    else:
        raise exc

codecs.register_error("test.custom_handler", custom_handler)
codecs.register_error("test.custom_handler_2", custom_handler_2)

# test utf-8
for encoding in ["utf-8", "utf_8"]:
    try:
        u"abc\u1234".encode(encoding, "test.custom_handler")
    except UnicodeEncodeError:
        print("failed to encode using %s with custom handler" % encoding)
