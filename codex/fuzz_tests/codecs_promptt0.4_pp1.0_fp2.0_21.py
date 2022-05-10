import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    return (u'', exception.start + 1)

codecs.register_error('test', handler)

def test(name, encoding):
    print '%s:' % name
    print '    ', codecs.lookup_error('test')
    print '    ', codecs.lookup_error(name)
    print '    ', codecs.lookup_error(encoding)

test('test', 'test')
test('test', 'test_error')
test('test_error', 'test')
test('test_error', 'test_error')
