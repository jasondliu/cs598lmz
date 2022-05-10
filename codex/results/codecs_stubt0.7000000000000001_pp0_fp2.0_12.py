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

def check_error_handling(name, input, errors):
    try:
        u = input.encode(name, errors)
    except UnicodeEncodeError as exc:
        print("UnicodeEncodeError:", exc.args)
        print("encoding:", exc.encoding)
        print("reason:", exc.reason)
        print("start:", exc.start)
        print("end:", exc.end)
        print("object:", exc.object)
        u = input.encode(name, "add_one_codepoint")
    print("*", name, errors)
    print("input:", input)
    print("result:", u)
    print("decoded back:", u.decode(name))
    print()

check_error_handling("ascii", "abc\u1234def", "strict")
check_error_handling("ascii", "abc\u1234def", "ignore")
check_error_handling("ascii", "abc\u1234def", "replace")
