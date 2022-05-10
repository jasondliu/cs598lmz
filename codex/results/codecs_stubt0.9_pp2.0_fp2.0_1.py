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

encode_module_names = [
    "ascii_module",
    "latin_1_module",
    "cp1252_module",
    "utf_8_module",
    "utf_16_le_module",
    "utf_16_be_module",
    "utf_16_ex_module",
    "utf_32_le_module",
    "utf_32_be_module",
    "utf_32_ex_module",
    "big5_module",
    "big5hkscs_module",
    "cp037_module",
    "cp424_module",
    "cp437_module",
    "cp500_module",
    "cp720_module",
    "cp737_module",
    "cp775_module",
    "cp850_module",
    "cp852_module",
    "cp855_module",
    "cp856_module",
    "cp857_module",
    "cp860_module",
    "cp861_module",
    "cp86
