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

def test_main():
    strs = []
    strs += [chr(i) for i in range(0, 0xd800)]
    strs += [chr(i) for i in range(0xe000, 0x10000)]

    # isolate high and low surrogates
    strs += ["".join(pair) for pair in itertools.product(
        [chr(i) for i in range(0xd800, 0xdc00)],
        [chr(i) for i in range(0xdc00, 0xe000)],
    )]

    for str in strs:
        # try out each codec for each string
        for codec in ["utf-8", "utf-16-le", "utf-16-be", "utf-32-le", "utf-32-be"]:
            try:
                encoded = str.encode(codec, "add_one_codepoint")
            except UnicodeEncodeError:
                pass
            else:
                # a new surrogate pair was added
                assert len(encoded) >= 4
               
