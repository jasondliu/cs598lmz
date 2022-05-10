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

input = [
     (b'\xc3\xa9', "add_one_codepoint", "utf-8"),
     (b'a\xc2a', "add_utf16_bytes", "utf-16"),
     (b'\x00a\x00a', "add_utf32_bytes", "utf-32"),
]

for input, error_handler_name, encoding in input:
    error_handler = getattr(codecs, error_handler_name)
    codecs.register_error(error_handler)
    print(codecs.decode(input, encoding, errors="strict"))
    codecs.decode(input, encoding, errors=error_handler)
    try:
       codecs.decode(input, encoding, errors="ignore")
    except UnicodeDecodeError:
        pass
    else:
        print("not failed for ignore")
