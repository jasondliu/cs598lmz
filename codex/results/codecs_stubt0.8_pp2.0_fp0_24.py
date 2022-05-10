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

encoding = 'utf-32-le'

def _check_decode(codec, data, errors, exp_len, exp_exc=None):
    if isinstance(data, str):
        data_str = data
    else:
        data_str = "".join("\\x{:02x}".format(ord(b)) for b in data)
    print("decoding {!r}/{!r} from {} with {}...".format(
        data, data_str, encoding, codec))
    try:
        decoded = codec.decode(data, errors=errors)
    except UnicodeDecodeError as e:
        if exp_exc is None:
            raise
        else:
            print("UnicodeDecodeError: {}/{!r}/{}".format(
                e.encoding, e.object, e.reason))
            pytest.fail("unexpected exception")
    else:
        if exp_exc is not None:
            raise exp_exc("expected exception, didn't get one")
        if len(decoded)
