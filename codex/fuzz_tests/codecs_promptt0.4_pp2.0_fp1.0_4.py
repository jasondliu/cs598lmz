import codecs
# Test codecs.register_error

# This test checks that codecs.register_error() works.

import codecs
import sys

# Error handler
def my_handler(exception):
    return ("test", exception.end)

# Register error handler
codecs.register_error("test.error", my_handler)

# Encode
print(codecs.charmap_encode("abc", "strict", "test.error"))
print(codecs.charmap_encode("abc", "replace", "test.error"))
print(codecs.charmap_encode("abc", "ignore", "test.error"))
print(codecs.charmap_encode("abc", "xmlcharrefreplace", "test.error"))
print(codecs.charmap_encode("abc", "backslashreplace", "test.error"))

# Decode
print(codecs.charmap_decode(b"abc", "strict", "test.error"))
print(codecs.charmap_decode(b"abc", "replace
