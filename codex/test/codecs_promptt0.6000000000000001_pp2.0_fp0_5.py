import codecs
# Test codecs.register_error:
def bad_decode_handler(exc):
    print("bad_decode_handler:", exc)
    return ("<bad_byte>", exc.end)
codecs.register_error("test.bad_decode", bad_decode_handler)
print(codecs.lookup_error("test.bad_decode"))
def bad_encode_handler(exc):
    print("bad_encode_handler:", exc)
    return ("<bad_char>", exc.end)
codecs.register_error("test.bad_encode", bad_encode_handler)
print(codecs.lookup_error("test.bad_encode"))
