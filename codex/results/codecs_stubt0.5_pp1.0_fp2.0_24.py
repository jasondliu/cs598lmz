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

#
# test encoding/decoding
#

def test_decode():
    for encoding in ("utf-8", "utf-16", "utf-32"):
        for errors in ("strict", "ignore", "replace", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"):
            for byteorder in (-1, 0, 1):
                if byteorder == 0 and encoding != "utf-8":
                    continue
                if byteorder == -1:
                    byteorder = "<"
                elif byteorder == 1:
                    byteorder = ">"
                else:
                    byteorder = "="
                name = "%s_%s_%s" % (encoding, byteorder, errors)
                yield check_decode, name, encoding, byteorder, errors

def check_decode(name, encoding, byteorder, errors):
    print("testing", name)
    try:
        decoder = codecs.getdecoder(encoding)
    except LookupError:
        # skip test for unknown
