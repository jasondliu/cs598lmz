import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

# Test UnicodeEncodeError

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32']:
    print '%s:' % encoding
    try:
        u'\u1234'.encode(encoding, 'test.ignore')
    except UnicodeEncodeError, err:
        print '  ', err

# Test UnicodeDecodeError

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32']:
    print '%s:' % encoding
    try:
        '\xff'.decode(encoding, 'test.ignore')
    except UnicodeDecodeError, err:
        print '  ', err

# Test UnicodeTranslateError

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-
