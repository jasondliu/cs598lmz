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

if __name__ == "__main__":
    import sys, string
    #    encoding = sys.argv[1]
    encoding = 'utf-8'
    file = "ucs-2-test.txt"
    text = open(file, "rb").read()
    print("original:")
    print("--------------------")
    print(text)
    print("--------------------\n")
    print("with add_one_codepoint error handler:")
    print("--------------------")
    print(text.decode(encoding, "add_one_codepoint"))
    print("--------------------\n")
    print("with add_utf16_bytes error handler:")
    print("--------------------")
    print(text.decode(encoding, "add_utf16_bytes"))
    print("--------------------\n")
    print("with add_utf32_bytes error handler:")
    print("--------------------")
    print(text.decode(encoding, "add_utf32_bytes"))
    print("--------------------\n")
