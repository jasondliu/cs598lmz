import codecs
# Test codecs.register_error
def my_replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        s = exc.object[exc.start:exc.end]
        return s.replace("\r", "?"), exc.end
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("myreplace", my_replace_error)

codecs.decode("\r", "myreplace")

# Test codecs.lookup_error
codecs.lookup_error("myreplace")("\xff", 0)

# Test codecs.escape_decode
codecs.escape_decode(b"\\x00\\x01")

# Test codecs.escape_encode
codecs.escape_encode(b"\x00\x01")

# Test codecs.raw_unicode_escape_decode
codecs.raw_unicode_escape_decode("\\u0020\\u1234")

# Test codecs.raw_unicode_escape
