import codecs
# Test codecs.register_error, ensure we don't recurse into
# ourselves too many times.
def bad_handler(e):
    raise UnicodeDecodeError("bad_handler called")

try:
    codecs.register_error("test.recursion", bad_handler)
except UnicodeEncodeError as e:
    print(repr(e))
else:
    raise RuntimeError("Didn't raise an exception")

# Test codecs.encode.
# With an uninitialised UnicodeEncodeError
try:
    codecs.encode("abc", "ascii", "ignore")
except UnicodeEncodeError as e:
    print(e.encoding)
    print(e.object)
    print(repr(e.reason))
    print(repr(e.start))
    print(repr(e.end))
    print(repr(e.object[e.start:e.end]))
    print(repr(e.args))
    print(repr(e))

# With an initialised UnicodeEncodeError
try:
    codecs.encode("
