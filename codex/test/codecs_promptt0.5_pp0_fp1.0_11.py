import codecs
# Test codecs.register_error

def codec_map_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        s = []
        for c in exc.object[exc.start:exc.end]:
            if ord(c) < 0x80:
                s.append(c)
            else:
                s.append("["+hex(ord(c))+"]")
        return (u"".join(s), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("test.codec_map_replace", codec_map_replace)

