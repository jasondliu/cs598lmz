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

c = CodecsHarness(add_one_codepoint, add_utf16_bytes, add_utf32_bytes)

run_test(c, "add_a")

def ignore_nothing(exc):
    return ('', exc.start)

def ignore_utf16_byte(exc):
    return ('', exc.start + 1)

def ignore_utf32_byte(exc):
    return ('', exc.start + 4)

codecs.register_error("ignore_nothing", ignore_nothing)
codecs.register_error("ignore_utf16_byte", ignore_utf16_byte)
codecs.register_error("ignore_utf32_byte", ignore_utf32_byte)

c = CodecsHarness(ignore_nothing, ignore_utf16_byte, ignore_utf32_byte)

run_test(c, "ignore_byte")

def sub_nothing(exc):
    return (u'\ufffd', exc.start)

def sub_utf16_byte(exc):
    return (u'\uff
