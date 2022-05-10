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

def test_decode_error(input, err_type, err_msg, err_pos, err_handler=None,
                      err_handler_args=None):
    try:
        input.decode("utf-8", err_handler)
    except UnicodeDecodeError as exc:
        assert exc.reason == err_type
        assert exc.object is input
        assert exc.start == err_pos
        if err_handler_args is None:
            assert exc.end == err_pos + 1
            assert exc.args[0] == err_msg % (err_pos, err_pos + 1)
        else:
            assert exc.end == err_pos + err_handler_args
            assert exc.args[0] == err_msg % (err_pos, err_pos + err_handler_args)
        return
    raise AssertionError("UnicodeDecodeError not raised")

def test_encode_error(input, err_type, err_msg, err_pos, err_handler=None,
                      err_handler_args=None):

