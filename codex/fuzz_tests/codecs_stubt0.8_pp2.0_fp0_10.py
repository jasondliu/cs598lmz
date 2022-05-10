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

# Test basic functionality
print("Test basic functionality")

s = "hello"
t = codecs.decode(s, "ascii", "add_one_codepoint")
assert t == "ahello", t

try:
    t = codecs.decode(s, "utf-16-be", "add_one_codepoint")
    raise Exception("shouldn't be able to decode utf-16-be with "
                    "add_one_codepoint")
except UnicodeDecodeError as inst:
    assert inst.reason == "add_one_codepoint", inst.reason
    assert inst.start == 0, inst.start

# Test that it still works when the input doesn't change
print("Test that it still works when the input doesn't change")

s = "hello"
t = codecs.decode(s, "ascii", "add_one_codepoint")
assert t == "ahello", t

# Test encoding
print("Test encoding")

s = "a"
t = codecs.encode(s
