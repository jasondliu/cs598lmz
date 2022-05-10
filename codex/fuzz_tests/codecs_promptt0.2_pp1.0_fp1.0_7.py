import codecs
# Test codecs.register_error()

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

# Test the 'ignore' error handler
for encoding in ('ascii', 'latin-1', 'utf-8'):
    print encoding, ':',
    try:
        print codecs.decode('\xff', encoding, 'test.ignore'),
    except UnicodeDecodeError, e:
        print 'UnicodeDecodeError',
    print

# Test the 'replace' error handler
for encoding in ('ascii', 'latin-1', 'utf-8'):
    print encoding, ':',
    try:
        print codecs.decode('\xff', encoding, 'replace'),
    except UnicodeDecodeError, e:
        print 'UnicodeDecodeError',
    print

# Test the 'xmlcharrefreplace' error handler
for encoding in ('ascii', 'latin-1', 'utf-8'):
    print encoding, ':',
    try:
        print
