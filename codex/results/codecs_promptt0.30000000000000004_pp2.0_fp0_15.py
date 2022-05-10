import codecs
# Test codecs.register_error(), which is used to register a custom error
# handler.

# This tests the default error handler.

import codecs
import sys

def test(encoding):
    try:
        codecs.lookup(encoding)
    except LookupError:
        print('SKIP %s: codec not found' % encoding)
        return

    # Encode a string with a character that cannot be represented in the
    # target encoding.
    s = 'abc\u1234def'
    try:
        b = s.encode(encoding)
    except UnicodeEncodeError:
        pass
    else:
        print('%s: expected UnicodeEncodeError' % encoding)

    # Decode a byte string with a byte that cannot be represented in the
    # target encoding.
    b = b'abc\x80def'
    try:
        s = b.decode(encoding)
    except UnicodeDecodeError:
        pass
    else:
        print('%s: expected UnicodeDecodeError' % encoding)

    # Decode a byte string with an incomplete character
