import codecs
# Test codecs.register_error

# This test is for the case where the error handler is registered for a
# specific encoding.

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.strict', handler)

# Now try to use it

def test(encoding):
    try:
        u'\x80'.encode(encoding)
    except UnicodeEncodeError, exc:
        if exc.end != 1:
            print 'Unexpected end', exc.end
            raise
    else:
        print 'No exception raised'

for encoding in ['ascii', 'latin-1', 'iso-8859-1', 'iso-8859-15',
                 'koi8-r', 'cp1251', 'cp866', 'mac-cyrillic']:
    test(encoding)

# Now try to use it with a stream

def teststream(encoding):
    try:
        codecs.getwriter(encoding)(sys.stdout).write(u'\x80')
