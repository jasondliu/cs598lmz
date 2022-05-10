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

def test_errors():
    def gen_output(s):
        for c in s:
            yield bytes((c,))

    assert next(gen_output("a\udce2b\udce2c")) == \
        b'a\xed\xb3\xa2b\xed\xb3\xa2c'
    assert next(gen_output("a\udce2b\udce2c"), "") == \
        b'a\xed\xb3\xa2b\xed\xb3\xa2c'
    assert next(gen_output("a\udce2b\udce2c"), "a") == \
        b'a\xed\xb3\xa2b\xed\xb3\xa2c'
    pytest.raises(StopIteration, next, gen_output(""))
    pytest.raises(StopIteration, next, gen_output(""), "a")
    assert next(gen_output("a"), "") == b'a'
    assert next(gen_output("a"), "b
