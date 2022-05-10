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

def test_decode_error_handling(input_type, input, errors):
    print("input_type:", input_type)
    print("input:", input)
    print("errors:", errors)

    if input_type == "string":
        input = input.encode("utf-8")

    try:
        print("unicode(input, 'utf-8', errors):", unicode(input, "utf-8", errors))
    except UnicodeDecodeError as e:
        print("unicode(input, 'utf-8', errors): raised UnicodeDecodeError")
        print("                           args:", e.args)
        print("                               e.start:", e.start)
        print("                               e.end:", e.end)
        print("                               e.object:", e.object)
        print("                               e.reason:", e.reason)
        print("                               e.encoding:", e.encoding)
        print("                               e.end:", e.end)

    print("")


def main():
