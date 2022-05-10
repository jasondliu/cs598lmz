import codecs
# Test codecs.register_error for 'replace', 'ignore' and the default
# (strict) handling.

def encode_bad_input(codec, s, exc, replace_val):
    msg = str(exc)
    actual = codecs.register_error(lambda x: replace_val)(exc)(s, 0, "")
    if replace_val is None:
        expected = (msg, 0)
    else:
        expected = (replace_val, len(s))
    assert actual == expected, "%s: got %r instead of %r" % (msg, actual, expected)

def test_encode_errors():
    # codecs.register_error()
    def bad_handler(exception):
        raise ValueError("bad!")

    codecs.register_error(bad_handler)
    raises(ValueError, "codecs.register_error(bad_handler)")

    codecs.register_error("replace")
    encode_bad_input("utf-8", "a\uDC00", UnicodeEncodeError("utf-8", u"a\uDC00", 0,
