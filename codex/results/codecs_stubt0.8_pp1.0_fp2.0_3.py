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

errors = ["ignore", "replace", "xmlcharrefreplace", "backslashreplace", "namereplace",
          "surrogateescape", "surrogatepass", "strict", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]

data = "Hello World\n"

fo = codecs.open("test402.txt", "w", "utf-32-be", errors = "strict")
fo.write(data)
fo.close()

fo = codecs.open("test402.txt", "r", "utf-32-be")
d = fo.read()
for error in errors:
    print
    print "========================= %s ========================" % error
    print "D: ", repr(d)
    print "E: ", repr(d.encode("latin-1", error))
    print "D: ", repr(d.decode("latin-1", error))
    print "E: ", repr(d.encode("ascii", error))
    print "D: ",
