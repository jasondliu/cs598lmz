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

encoding = "utf-8"

def check(ucs2_string, bytes_string, errors):
    # check encode
    encoded, bytes_consumed = codecs.utf_16_be_encode(ucs2_string+u"abc", errors)
    assert bytes_consumed == len(ucs2_string)
    assert encoded == bytes_string

    # check decode
    decoded, bytes_consumed = codecs.utf_32_be_decode(bytes_string+b"1234", errors)
    assert bytes_consumed == len(bytes_string)
    assert decoded == ucs2_string

    # check stream reader
    reader = codecs.getreader("utf-16-be")
    stream = reader(StringIO(bytes_string))
    assert stream.read() == ucs2_string

    # check stream writer
    writer = codecs.getwriter("utf-32-be")
    stream = StringIO()
    writer(stream, errors).write(ucs2_string)
    assert stream.getvalue() == bytes
