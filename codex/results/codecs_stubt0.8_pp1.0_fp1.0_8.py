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

def test(encoding):
    print(encoding, "->", encoding, end=' ')
    try:
        encoder = codecs.getencoder(encoding)
        decoder = codecs.getdecoder(encoding)
    except LookupError:
        print("not supported")
        return
    try:
        # encode to bytes
        data1 = encoder("abc\u1234")[0]
        # decode to string
        data2 = decoder(data1, "add_one_codepoint")[0]
        print("okay")
    except UnicodeDecodeError as e:
        # Shouldn't happen
        print(e)

test("utf-8")
test("utf_8_sig")
test("utf-16")
test("utf_16_be")
test("utf_16_le")
test("utf-16-be")
test("utf-16-le")
test("utf-32")
test("utf_32_be")
test("utf_32_le")
test("utf-32-be
