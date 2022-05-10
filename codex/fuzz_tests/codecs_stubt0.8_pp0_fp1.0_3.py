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
    codecs.lookup_error("foobar")
except LookupError as e:
    print(e)

print(codecs.lookup_error("replace").name)
print(codecs.lookup_error("xmlcharrefreplace").name)
print(codecs.lookup_error("strict"))
print(codecs.lookup_error("ignore"))
print(codecs.lookup_error("backslashreplace").name)
print(codecs.lookup_error("namereplace").name)
print(codecs.lookup_error("add_one_codepoint").name)
print(codecs.lookup_error("ignore").name)
print(codecs.lookup_error("surrogateescape").name)

def bad_handler(*args, **kwargs):
    raise RuntimeError("custom handler raised this error")

codecs.register_error("bad_handler", bad_handler)
codecs.lookup_error("bad_handler")

try:
    codecs.
