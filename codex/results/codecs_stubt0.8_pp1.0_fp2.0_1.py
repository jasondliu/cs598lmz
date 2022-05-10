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

#
# Test decoding with the "add_one_codepoint" error handler
# All characters are copied verbatim, with the exception of
# the first character which is converted to "a".
#

for encoding in ["ascii", "utf-8", "utf-16", "utf-32"]:
    title = "UnicodeError with handler 'add_one_codepoint' (decoding, %s)" % encoding
    print(title)
    inp = "abcdé✓"
    res = codecs.decode(inp.encode(encoding), encoding, "add_one_codepoint")
    if res != "a".encode(encoding):
        print("Failed: res=", repr(res))


#
# Test encoding with the "add_one_codepoint" error handler
# All characters are copied verbatim, with the exception of
# the first character which is converted to "a".
#

for encoding in ["ascii", "utf-8", "utf-16", "utf-32"]:
   
