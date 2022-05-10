import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

# Test that the error handler is called

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Testing encoding', encoding
    for input, expected in [
        ('abc\xffdef', u'abcdef'),
        ('abc\xff\xffdef', u'abcdef'),
        ('abc\xff\xff\xffdef', u'abcdef'),
        ('abc\xff\xff\xff\xffdef', u'abcdef'),
        ('abc\xff\xff\xff\xff\xffdef', u'abcdef'),
        ('abc\xff\xff\xff\xff\xff\xffdef', u'abcdef'),
        ('abc\xff\xff\xff\xff\xff\xff\xffdef', u'abcdef'),
        ('abc\xff\xff\xff\xff\xff\xff\xff\xffdef', u'abcdef'),
        ('abc\xff
