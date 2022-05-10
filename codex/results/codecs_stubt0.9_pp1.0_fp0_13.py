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

def buggy_read_utf16(checks, encoder, decoder, input, output, errors="strict"):
    u = codecs.getreader("utf-16")(io.BytesIO(input))
    check(checks, encoder(u.read()))
    u.seek(0)
    check(checks, encoder(u.read(2)))
    u.seek(0)
    check(checks, encoder(u.readline()))
    u.seek(0)
    check(checks, encoder(u.readline(2)))
    # Check the surrogates handling in the incremental decoder
    f = codecs.getreader("utf-16")(io.BytesIO(input), errors="strict")
    while True:
        s = f.read(2)
        if not s:
            break
        check(checks, encoder(s))
    # Check the surrogates handling in the incremental decoder
    f = codecs.getreader("utf-16")(io.BytesIO(input), errors="replace")
    while True:
       
