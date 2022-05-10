import codecs
# Test codecs.register_error()
def bad_encode(e):
    raise UnicodeEncodeError("bad_encode", e.object, e.start, e.end, "bad_encode")
def bad_decode(e):
    raise UnicodeDecodeError("bad_decode", e.object, e.start, e.end, "bad_decode")
def bad_replace(e):
    raise UnicodeDecodeError("bad_replace", e.object, e.start, e.end, "bad_replace")
