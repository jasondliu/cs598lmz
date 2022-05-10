import codecs
# Test codecs.register_error

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

# Test that the error handler is called
s = u'\u20ac\u20ac\u20ac'
for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32']:
    try:
        s.encode(encoding, 'test.ignore')
    except UnicodeEncodeError:
        print 'UnicodeEncodeError:', encoding

# Test that the error handler is called
for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32']:
    try:
        codecs.encode(s, encoding, 'test.ignore')
    except UnicodeEncodeError:
        print 'UnicodeEncodeError:', encoding

# Test that the error handler is called
for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-
