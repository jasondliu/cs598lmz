import codecs
# Test codecs.register_error()

# This test should be run with the -u command line option

import sys
if sys.stdout.encoding != 'UTF-8':
    raise RuntimeError("expected sys.stdout.encoding to be 'UTF-8'")
if sys.stderr.encoding != 'UTF-8':
    raise RuntimeError("expected sys.stderr.encoding to be 'UTF-8'")

def f(exc):
    if exc.object[exc.start:exc.end] != '\udc80':
        raise RuntimeError("expected object[start:end] to be '\\udc80'")
    return (u'\u1234', exc.end)

codecs.register_error('test.notfound', f)

def test(encoding):
    s = '\udc80'.decode(encoding, 'test.notfound')
    if s != u'\u1234':
        raise RuntimeError("expected '\\u1234', got %r" % s)

test('ascii')
test('iso8859
