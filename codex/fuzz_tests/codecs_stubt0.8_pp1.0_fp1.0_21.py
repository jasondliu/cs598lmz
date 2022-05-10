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

# Error handler
def xmlcharrefreplace(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeTranslateError)):
        s = [u"&#%d;" % ord(c) for c in exc.object[exc.start:exc.end]]
        return ("".join(s), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

# Bad data
for data in (b'\xe4\xbf\xa1\xe6\x81\xaf',
             b'\xe4\xbf\xa1\xe6\x81\xaf\xe7\xbb\x93\xe6\x9e\x84'
             b'\xe7\xbb\x93\xe6\x9e\x843\xe6\x96\xb9\xe9\x87\x8f'
             b'\xe5\x8c\x96\xe7\xbb\x93\xe6\x9e\x843\
