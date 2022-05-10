import codecs
# Test codecs.register_error()

import codecs
import encodings

def search_function(encoding):
    if encoding == "test.unicode":
        return codecs.lookup("utf-8")
    return None

codecs.register(search_function)

# Test that the codec is found
assert encodings.search_function("test.unicode") is not None

# Test that the codec is actually used
assert codecs.encode("abc", "test.unicode") == b"abc"

# Test that the codec is actually used
assert codecs.decode(b"abc", "test.unicode") == "abc"

# Test that the codec is actually used
assert codecs.escape_encode(b"abc")[0] == b"abc"

# Test that the codec is actually used
assert codecs.escape_decode(b"abc")[0] == b"abc"

# Test that the codec is actually used
assert codecs.escape_encode(b"abc")[0] == b"abc"

# Test that the codec is
