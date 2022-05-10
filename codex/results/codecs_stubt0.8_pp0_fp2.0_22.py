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

for encoding in "utf-8 utf-16 utf-32".split():
    print("Codec CodecError FallbackError: %20s" % encoding, end=' ')
    s = "a\udc80\udcff"
    try:
        print(s.encode(encoding))
    except Exception as e:
        print(e.__class__.__name__)

    print("Codec xback CodecError FallbackError: %20s" % encoding, end=' ')
    try:
        print(s.encode(encoding, "xback"))
    except Exception as e:
        print(e.__class__.__name__)

    print("Codec xback 'add_one_codepoint': %20s" % encoding, end=' ')
    try:
        print(s.encode(encoding, "xback", "add_one_codepoint"))
    except Exception as e:
        print(e.__class__.__name__)

    if encoding in ('utf-16', 'utf-32'):
