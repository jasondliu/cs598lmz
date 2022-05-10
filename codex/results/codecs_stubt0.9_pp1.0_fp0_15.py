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

def test(name, codec, errors):
    print(codec, "utf-8 encode, error:", errors)
    # initialize the decoder
    for s in [b"abc", b"abc\xd0\x00\xd1\x00", b"abc\x00\xd0\x00\xd1"]:
        print("  input:", s)
        try:
            s.decode(codec+"_"+errors[0])
            print("  forward", end=" ")
        except Exception as e:
            print("**EXCEPTION**", e)
            return
        try:
            s.decode(codec+"_"+errors[0], "strict")
            print("  strict (forward)", end=" ")
        except Exception as e:
            print("**EXCEPTION**", e)
            return
        print()

test("skip", "utf_16", ["ignore"])
test("add_one", "utf_16", ["replace"])
test("add_bytes", "utf_16", ["add_
