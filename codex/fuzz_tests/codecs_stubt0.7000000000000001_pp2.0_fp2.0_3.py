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

# unicode-internal-encode-error
print("unicode-internal-encode-error")

for enc in ["utf-8", "utf-16", "utf-32"]:
    print("\n*** Encoding with %s:" % enc)
    text = "ab\uffff"
    print("Original text:", text)

    try:
        x = text.encode(enc)
    except UnicodeEncodeError as exc:
        print("UnicodeEncodeError:", exc.reason)
        print("encoding:", exc.encoding)
        print("end:", exc.end)
        print("object:", exc.object)
        print("start:", exc.start)
        print("")
        print("Adding one codepoint:", text.encode(enc, "add_one_codepoint"))
        print("Adding two UTF-8 bytes:", text.encode(enc, "add_utf8_bytes"))
        print("Adding two UTF-16 bytes:", text.encode(enc, "add_utf16_bytes"))
