import codecs
# Test codecs.register_error

# This test should be run with the -u command line option.

import sys
if sys.flags.unicode:
    print('Test skipped: cannot test codecs.register_error with unicode enabled')
    sys.exit(0)

import codecs

def handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('test.replace', handler)

text = 'abc\xffdef\u0100ghi'

assert codecs.decode(text, 'ascii', 'test.replace') == u'abc\ufffddef\ufffdghi'
assert codecs.decode(text, 'ascii', 'test.replace') == u'abc\ufffddef\ufffdghi'

assert codecs.decode(text, 'ascii', 'test.replace') == u'abc\ufffddef\ufffdghi'
assert codecs.decode(text, 'ascii', 'test.replace') == u'abc\ufffddef\ufffdgh
