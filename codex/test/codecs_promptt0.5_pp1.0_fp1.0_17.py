import codecs
# Test codecs.register_error()

def handler(exception):
    print("handler:", exception)
    return ("?", exception.end)

codecs.register_error("test.lookup", handler)

s = "abc\uFFFDdef\uFFFDghi"
print(s)
print(s.encode("ascii", "test.lookup"))
print(s.encode("ascii", "backslashreplace"))
print(s.encode("ascii", "xmlcharrefreplace"))
print(s.encode("ascii", "ignore"))
print(s.encode("ascii", "replace"))
