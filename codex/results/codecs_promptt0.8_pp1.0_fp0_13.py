import codecs
# Test codecs.register_error
a = (1, 2)
try:
    raise ValueError(*a)
except ValueError as e:
    print("Exception:", e)
    print("Encoding:", codecs.register_error("foobar", None)(u"\u1234", e) )

# EncodeError and the UnicodeTranslateError alias
try:
    raise UnicodeTranslateError(*a)
except UnicodeTranslateError as e:
    print("Exception:", e)
    print("Encoding:", codecs.register_error("foobar", None)(u"\u1234", e) )

# DecodeError
try:
    raise UnicodeDecodeError(*a)
except UnicodeDecodeError as e:
    print("Exception:", e)
    print("Encoding:", codecs.register_error("foobar", None)(u"\u1234", e) )
