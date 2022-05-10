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

# test the 3 error handlers
fc = codecs.getreader("utf-8")
ft = codecs.getreader("utf-16")
fu = codecs.getreader("utf-32")

data = b'abcd\x80\xff'

# utf-8: test the 3 error handlers
s = fc(io.BytesIO(data), "add_one_codepoint")
e = s.read()
print("s = %r" % (e,))
assert e == "abcd\x80a"

s = fc(io.BytesIO(data), "add_utf16_bytes")
e = s.read()
print("s = %r" % (e,))
assert e == "abcd\x80\xff"

s = fc(io.BytesIO(data), "add_utf32_bytes")
e = s.read()
print("s = %r" % (e,))
assert e == "abcd\x80\xff"

# utf-16: test the 3 error handlers
s = ft
