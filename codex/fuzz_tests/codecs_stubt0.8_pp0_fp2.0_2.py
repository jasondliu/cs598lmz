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

# Read UTF-16 from test-input/test_utf16_exception
# Write UTF-16 to test-output/test_utf16_exception_16
f_in = codecs.open("test-input/test_utf16_exception", 'r', "utf-16le", "add_one_codepoint")
f_out = codecs.open("test-output/test_utf16_exception_16", 'w', "utf-16le")
for i in range (0, 5):
    s = f_in.readline()
    f_out.write(s)
f_out.close()

# Read UTF-16 from test-input/test_utf16_exception
# Write UTF-8 to test-output/test_utf16_exception_8
f_in = codecs.open("test-input/test_utf16_exception", 'r', "utf-16le", "add_one_codepoint")
f_out = codecs.open("test-output/test_utf16_exception_8", 'w
