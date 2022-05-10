import codecs
# Test codecs.register_error

import codecs

def test(name, enc):
    try:
        u = unicode(name, enc)
    except UnicodeError, detail:
        print '%s: %s' % (enc, detail)
        return
    print '%s: %s' % (enc, u)

test('abc', 'ascii')
test('abc', 'latin-1')
test('abc', 'iso-8859-1')
test('abc', 'iso-8859-2')
test('abc', 'iso-8859-15')
test('abc', 'koi8-r')
test('abc', 'utf-8')
test('abc', 'utf-16')
test('abc', 'utf-16-le')
test('abc', 'utf-16-be')
test('abc', 'utf-32')
test('abc', 'utf-32-le')
test('abc', 'utf-32-be')

print 'registering error handler'

def my_error(exception):
    print 'my_error called with %r' %
