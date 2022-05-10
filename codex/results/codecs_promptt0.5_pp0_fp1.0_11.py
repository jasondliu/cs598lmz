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

decode = codecs.getdecoder("test.codec_map_replace")

s = u"\u3042\u3044\u3046\u3048\u304a"

for i in range(len(s)):
    for j in range(i, len(s)):
        print decode(s[i:j])
