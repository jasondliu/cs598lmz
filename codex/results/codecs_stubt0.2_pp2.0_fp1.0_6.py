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

def test_main():
    # Test UTF-16
    for enc in ("utf-16", "utf-16-le", "utf-16-be"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint",
                       "add_utf16_bytes"):
            for input, expected in [
                (b"\xff", "�"),
                (b"\xff\xff", "����"),
                (b"\xff\xff\xff", "�����"),
                (b"\xff\xff\xff\xff", "��������"),
                (b"\xff\xff\xff\xff\xff", "���������"),
                (b"\xff\xff\xff\xff\xff\xff", "������������"),
                (b"\xff\xff\xff\xff\xff\xff\xff", "�������������"),
                (b"\xff\xff\xff\xff\xff\xff\xff\xff", "����������������"),
                (b"\xff\xff\xff\xff\xff\xff
