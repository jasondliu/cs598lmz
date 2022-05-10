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

# Test the default behaviour of the codecs module

# We're using the 'replace' error handler here because it is the default
# one and because it is the only one that doesn't raise an exception
# (which we're testing here).

# Test the codecs module with the 'replace' error handler

print("Testing the codecs module with the 'replace' error handler")

# Encoding

# Test encoding a single character
print("\nEncoding a single character")

try:
    print(codecs.encode("\xe9", "ascii"))
except UnicodeEncodeError:
    print("Failed")
else:
    print("Succeeded")

try:
    print(codecs.encode("\xe9", "latin1"))
except UnicodeEncodeError:
    print("Failed")
else:
    print("Succeeded")

try:
    print(codecs.encode("\xe9", "utf-8"))
except UnicodeEncodeError:
    print("Failed")
else:
    print
