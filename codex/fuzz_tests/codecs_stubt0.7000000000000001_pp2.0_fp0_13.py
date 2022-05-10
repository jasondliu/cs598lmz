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

def test_single_value(exc):
    return True

def test_replace_replace(exc):
    return (True, exc.start + 1)

codecs.register_error("test_single_value", test_single_value)
codecs.register_error("test_replace_replace", test_replace_replace)

class Test_UnicodeDecodeError:
    def test_init(self):
        e = UnicodeDecodeError("utf8", b"bytes", 1, 2, "reason")
        assert e.encoding == 'utf8'
        assert e.object == b"bytes"
        assert e.start == 1
        assert e.end == 2
        assert str(e) == "'utf8' codec can't decode bytes in position 1-2: reason"

    def test_init_msg(self):
        e = UnicodeDecodeError("utf8", b"bytes", 1, 2, "reason")
        assert e.msg == "reason"

    def test_init_object_type(self):
        e = UnicodeDecodeError("
