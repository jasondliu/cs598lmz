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
encoding_table = (
    u"\u041a\u0432\u0430\u0442\u043e\u0440" # Cyrillic
    u"\u0628\u0644\u0627\u0633\u0647" # Arabic
    u"\u092f\u0939\u093f\u0915\u094d\u0937\u093e" # Devanagari
    u"\u4e2d\u6587" # Hànzì (Chinese)
    u"\x00\x01\x02\x03\x04" # ASCII
    u"\ufffd" # Replacement character
)

def sample_error_handlers():
    print("\nError:'add_one_codepoint':\n")
    for enc in 'utf-16', 'utf-32':
        print("{0:.<15}{0:>15}".format("".join("{0} ".format(hex(c))[2:].rjust(12, '0')
