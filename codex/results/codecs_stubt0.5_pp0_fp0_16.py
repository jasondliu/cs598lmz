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

# test the error handlers with the surrogateescape error handler

# test with UTF-8
with codecs.open("surrogatepass_codecs_crash.txt", encoding="utf-8", errors="surrogateescape") as fp:
    for line in fp:
        pass

# test with UTF-16
with codecs.open("surrogatepass_codecs_crash.txt", encoding="utf-16", errors="surrogateescape") as fp:
    for line in fp:
        pass

# test with UTF-32
with codecs.open("surrogatepass_codecs_crash.txt", encoding="utf-32", errors="surrogateescape") as fp:
    for line in fp:
        pass

# test the error handlers with the add_one_codepoint error handler

# test with UTF-8
with codecs.open("surrogatepass_codecs_crash.txt", encoding="utf-8", errors="add_one_codepoint") as fp:
    for line
