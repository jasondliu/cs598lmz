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

def run_test(name, data, enc, dec, errors):
    try:
        print("Testing %s" % name)
        print("Encoding:", end=' ')
        encoded = data.encode(enc, errors)
        print(repr(encoded))
        print("Decoding:", end=' ')
        decoded = encoded.decode(dec, errors)
        print(repr(decoded))
        if decoded != data:
            print("ERROR: decoding failed")
            print("Expected:", repr(data))
        print()
    except Exception as e:
        print("ERROR:", e)
        print()

data = "abc"

run_test("UTF-8 to UTF-8", data, "utf-8", "utf-8", "strict")
run_test("UTF-8 to UTF-8", data, "utf-8", "utf-8", "replace")
run_test("UTF-8 to UTF-8", data, "utf-8", "utf-8", "ignore")
run_test("UTF
