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
try:
    codecs.decode("\u1D11E\u1234\u4321", "utf-8", "surrogatepass")
except UnicodeError as exc:
    print(exc)
    print(exc.object)
    print(exc.args)
    print(exc.start)
    print(exc.end)
    print(exc.reason, exc.object[exc.start])
    print(exc.object[exc.start:exc.end])

print(codecs.decode("\u1D11E\u1234\u4321", "utf-8", "add_one_codepoint"))
print(codecs.decode(b'\xf0\x9d\x84\x9e\xd1\x88\xd2\x94\xd3\x81\xd2\xa1', "utf-8", "add_utf16_bytes"))
print(codecs.decode(b'\xf0\x9d\x84\x9e\xf0\x92\x88\x
