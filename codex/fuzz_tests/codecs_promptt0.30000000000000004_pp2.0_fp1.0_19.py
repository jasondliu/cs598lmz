import codecs
# Test codecs.register_error

def handler(exception):
    print("handler called", exception)
    return "", exception.end

codecs.register_error("test.lookup", handler)

encoding = "test.lookup"

# Test with a unicode string
s = "abc\u20ac\u20acdef"
print(s.encode(encoding, "strict"))
print(s.encode(encoding, "replace"))
print(s.encode(encoding, "ignore"))
print(s.encode(encoding, "xmlcharrefreplace"))
print(s.encode(encoding, "backslashreplace"))

# Test with a bytes string
s = b"abc\xe2\x82\xac\xe2\x82\xacdef"
print(s.decode(encoding, "strict"))
print(s.decode(encoding, "replace"))
print(s.decode(encoding, "ignore"))
print(s.decode(encoding, "xmlcharrefreplace"))
print(s.decode
