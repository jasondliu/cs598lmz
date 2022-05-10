import codecs
# Test codecs.register_error
def handle_error(exc):
    if isinstance(exc, UnicodeEncodeError):
        text = u'ASCII encoding error: '
    elif isinstance(exc, UnicodeDecodeError):
        text = u'ASCII decoding error: '
    else:
        raise TypeError("don't know how to handle %r" % exc)
