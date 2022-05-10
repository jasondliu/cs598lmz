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

encode_hm = {b"abc": b"abc",
             b"\xff\xfe\x00x\x00\x00\x00\x01": b"x\x00\x00\x00\x01"}

decode_hm = {b"abc": "abc",
             b"x\x00\x00\x00\x01": b"\xff\xfe\x00x\x00\x00\x00\x01"}

def test_main(verbose=None):
    from test.test_support import run_suite, check_impl_detail

    check_impl_detail()
    run_suite(__name__)

if __name__ == '__main__':
    test_main()
