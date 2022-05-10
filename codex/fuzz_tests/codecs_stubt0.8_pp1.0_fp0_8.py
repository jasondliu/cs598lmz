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

def check_decode(tests):
    for str, (encoding, errors, out, exception) in tests:
        try:
            val = str.decode(encoding, errors)
            assert val == out, (val, out)
        except UnicodeError as e:
            assert e.args[0] == exception, e.args[0]

def check_encode(tests):
    for (str, out), (encoding, errors, exception) in tests:
        try:
            val = str.encode(encoding, errors)
            assert val == out, (val, out)
        except UnicodeError as e:
            assert e.args[0] == exception, e.args[0]

def check_float(encoding):
    encoding.decode("a", "strict")

def check_streamreader(reader, str, out):
    try:
        val = reader.read()
        assert val == out, (val, out)
    except UnicodeError as e:
        assert e.args[0] == exception, e.args[0
