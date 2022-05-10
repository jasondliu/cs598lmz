import codecs
# Test codecs.register_error, see SF bug #617225

try:
    import encodings.ascii
except ImportError:
    raise TestSkipped("not available on this platform")

def ascii_replace(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %s" % exc.__class__.__name__)
    return (u'?', exc.end), u'ascii'

def ascii_ignore(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %s" % exc.__class__.__name__)
    return (u'', exc.end), u'ascii'

class AsciiReplaceTest:
    errors = 'ascii_replace'

def test():
    s = u'\u12345'
    # first check raw ascii encoding (replace)
    if s.encode('ascii', 'ascii_replace') != '?ascii':
        print(
