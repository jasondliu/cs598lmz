import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print('[%s] %s' % (exception.__class__.__name__, exception))
    return u'\ufffd', exception.end

codecs.register_error('test.handler', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print('Encoding:', encoding)
