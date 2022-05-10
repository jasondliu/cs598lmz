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

check_symbols = '(u"\\x00\\x00", u"\\ufffd\\x00")*3+(u"\\u0041\\u007f123\u4f60\u597d", u"\\u0041\\u007f123\u4f60\ufffd")'
for from_enc, to_enc in zip(["utf-32","utf-16", "utf-8"], ["utf-8", "utf-32", "utf-16"]):
    x = u"\u03761123\u4f60\u597d" # it's unlikely that the last two chars would be the same in any encoding
    y = x.encode(from_enc, "add_one_codepoint")
    z = y.decode(to_enc, "replace")
    print("{}->{}->{} "
         "{}: {}\n{}: {}".format(x, y, z,
                                 from_enc, list(y), to_enc, list(z)))
    assert eval(check_symbols) == tuple(
