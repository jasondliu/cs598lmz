import codecs
# Test codecs.register_error

import codecs

def bad_decode_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        print('bad_decode_error called with %s' % exc)
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def bad_encode_error(exc):
    if isinstance(exc, UnicodeEncodeError):
        print('bad_encode_error called with %s' % exc)
        return (u'\ufffd'.encode('utf-8'), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

def bad_recursive_error(exc):
    if isinstance(exc, UnicodeEncodeError):
        print('bad_recursive_error called with %s' % exc)
        return (u'\ufffd'.encode('utf-8'), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc
