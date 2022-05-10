import codecs
# Test codecs.register_error

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        s = [u'\ufffd'] * len(exc.object[exc.start:exc.end])
        return (u''.join(s), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error("my_replace", my_replace)

# test UnicodeDecodeError
s = '\x81\x82\x83\x84'
for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    try:
        s.decode(encoding, 'my_replace')
    except UnicodeDecodeError, exc:
        assert exc.object is s
        assert exc.encoding == encoding
        assert exc.start == 0
        assert exc.end == len(s)

# test UnicodeEncodeError
s = u'\u1234\u5678'
for encoding in ['ascii', '
