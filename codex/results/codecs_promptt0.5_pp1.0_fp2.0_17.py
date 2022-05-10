import codecs
# Test codecs.register_error()

def handler(exception):
    print 'error', exception
    return u'\ufffd', exception.end

codecs.register_error('test', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print encoding,
    try:
        print codecs.decode('\xff', encoding, 'test')
    except UnicodeDecodeError, e:
        print 'UnicodeDecodeError', e
