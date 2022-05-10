import codecs
# Test codecs.register_error()
def hex_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        s = [ "%X" % ord(c) for c in exc.object[exc.start:exc.end] ]
        return (u"".join(s), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)
codecs.register_error("hex_replace", hex_replace)

def hex_decode(s):
    return s.decode("utf-8", "hex_replace")

def hex_encode(u):
    return u.encode("utf-8", "hex_replace")

# Test codecs.register_error()
def hex_replace_2(exc):
    if isinstance(exc, UnicodeDecodeError):
        s = [ "%X" % ord(c) for c in exc.object[exc.start:exc.end] ]
        return (u"".join(s), exc.end)
