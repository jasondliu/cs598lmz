import codecs
# Test codecs.register_error()

# This test is defined in the Python 3.2 docs:
# http://docs.python.org/dev/library/codecs.html#error-handlers

import codecs

def replace_error(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'\ufffd', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('test.replace', replace_error)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    try:
        u = u'pi: \u03c0'
        b = u.encode(encoding)
        print(b.decode(encoding, 'test.replace'))
    except UnicodeError as exc:
        print("{}: {}".format(encoding, exc))

