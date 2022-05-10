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

def print_error_handler_state(exc):
    print("encoding:", exc.encoding)
    print("object:", exc.object)
    print("start:", exc.start)
    print("end:", exc.end)
    print("reason:", exc.reason)
    print("strict:", exc.strict)
    print("end:", exc.end)

def print_unicode_error_state(exc):
    print("encoding:", exc.encoding)
    print("object:", exc.object)
    print("start:", exc.start)
    print("end:", exc.end)
    print("reason:", exc.reason)
    print("object[start:end]:", exc.object[exc.start:exc.end])

def print_unicode_translate_error_state(exc):
    print("object:", exc.object)
    print("start:", exc.start)
    print("end:", exc.end)
    print("reason:", exc.reason)
    print("object[
