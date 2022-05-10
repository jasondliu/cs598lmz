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

def test_error_callback(encoding):
    s = chr(0xdc00)
    try:
        s.encode(encoding)
    except UnicodeEncodeError as exc:
        s.encode(encoding, "add_one_codepoint")
    except UnicodeError:
        pass
    except Exception as exc:
        raise AssertionError("encode() raised wrong exception: " + str(exc))
    else:
        raise AssertionError("encode() didn't raise exception")

def test_error_callback_with_bytes(encoding):
    try:
        b'\x00'.decode(encoding)
    except UnicodeDecodeError as exc:
        b'\x00\x00'.decode(encoding, "add_utf16_bytes")
    except UnicodeError:
        pass
    except Exception as exc:
        raise AssertionError("decode() raised wrong exception: " + str(exc))
    else:
        raise AssertionError("decode() didn't raise exception")

def test_
