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

def analyzeASCII(text):
    for i in range(0x7f):
        if i not in text:
            print("Unassigned: %#x" % i)
    for i in range(0x7f, 0x100):
        print("Not ASCII: %#x" % i)

def analyzeUTF8(text):
    i = 0
    while i < len(text):
        c = text[i]
        cLen = 0
        if c & 0x80 == 0:
            print("ASCII: %#x" % c)
            cLen = 1
        elif c & 0xE0 == 0xC0:
            print("U+%04x" % c)
            cLen = 2
        elif c & 0xF0 == 0xE0:
            print("U+%04x" % c)
            cLen = 3
        elif c & 0xF8 == 0xF0:
            print("U+%04x" % c)
            cLen = 4
        else:
            print("
