import codecs
# Test codecs.register_error()

def bad_decode(input, errors='strict'):
    raise UnicodeDecodeError("bad", input, 0, 1, "bad")

def bad_encode(input, errors='strict'):
    raise UnicodeEncodeError("bad", input, 0, 1, "bad")

def good_decode(input, errors='strict'):
    return u"good", len(input)

def good_encode(input, errors='strict'):
    return "good", len(input)

def test_main():
    # Try/except is used to hide the traceback in PyPy
    try:
        codecs.register_error("test.bad", bad_decode)
        codecs.register_error("test.bad", bad_encode)
        codecs.register_error("test.good", good_decode)
        codecs.register_error("test.good", good_encode)
    except Exception:
        import traceback
        traceback.print_exc()
        raise SystemExit(1)
    # Test Unicode
