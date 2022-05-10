import codecs
# Test codecs.register_error, ensure we don't recurse into
# ourselves too many times.
def bad_handler(e):
    raise UnicodeDecodeError("bad_handler called")

try:
    codecs.register_error("test.recursion", bad_handler)
except UnicodeEncodeError as e:
    print(repr(e))
