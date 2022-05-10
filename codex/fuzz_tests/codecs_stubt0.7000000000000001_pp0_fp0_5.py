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

def check_error_handling(input, errors):
    for error in errors:
        try:
            codecs.decode(input, "ascii", error)
        except UnicodeDecodeError as exc:
            print(exc)
            print(error, input, exc.end)
        else:
            print("no error handler called")

check_error_handling(b'\x80', ["ignore", "replace", "backslashreplace", "namereplace", "xmlcharrefreplace", "surrogateescape", "surrogatepass", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"])
check_error_handling(b'\x80\x80', ["ignore", "replace", "backslashreplace", "namereplace", "xmlcharrefreplace", "surrogateescape", "surrogatepass", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"])
check_error_handling(b'\xff', ["ignore", "replace", "
