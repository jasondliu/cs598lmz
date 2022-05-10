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

# test utf-8
for i in range(0x80, 0x100):
    print(i)
    try:
        chr(i).encode("utf-8")
    except UnicodeEncodeError as e:
        print(e)
        print(e.object)
        print(e.start)
        print(e.end)
        print(e.reason)
        print(e.object[e.start:e.end])
        print(e.object.encode("utf-8", "add_one_codepoint"))

# test utf-16
for i in range(0x10000, 0x10200):
    print(i)
    try:
        chr(i).encode("utf-16")
    except UnicodeEncodeError as e:
        print(e)
        print(e.object)
        print(e.start)
        print(e.end)
        print(e.reason)
        print(e.object[e.start:e.end])
        print(e.object.encode
