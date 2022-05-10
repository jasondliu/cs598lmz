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

# UTF-8
encoding = "utf-8"
for error_handler in ["strict", "ignore", "replace", "surrogateescape"]:
    print(error_handler)
    f = codecs.open("testfile", "r", encoding, errors=error_handler)
    print(f.read())
    codecs.register_error("strict", None)
    codecs.register_error("ignore", None)
    codecs.register_error("replace", None)
    codecs.register_error("surrogateescape", None)
    
# UTF-16
encoding = "utf-16"
for error_handler in ["strict", "ignore", "replace", "surrogateescape"]:
    print(error_handler)
    f = codecs.open("testfile", "r", encoding, errors=error_handler)
    print(f.read())
    codecs.register_error("strict", None)
    codecs.register_error("ignore", None)
    codecs.register_error("replace", None)
    codecs
