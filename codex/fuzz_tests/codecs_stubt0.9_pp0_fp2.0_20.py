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

c = codecs.getincrementalencoder("hex")()
print(c.encode("abc"))
print(c.encode("def"))
print(c.encode("ghi"))
print(c.encode("jkl"))
print(c.encode("mno"))
print(c.encode("pqr"))
print(c.encode("stu"))
c.reset()
print(c.encode("vwx"))
c.reset()
print(c.encode("yz"))
c.reset()

c = codecs.getincrementalencoder("hex")()
print(c.encode("abc", "add_one_codepoint"))
c.reset()
print(c.encode("abc", "add_utf16_bytes"))
c.reset()
print(c.encode("abc", "add_utf32_bytes"))
c.reset()
