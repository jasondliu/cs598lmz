import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print(exception)
    return ('', exception.end)

codecs.register_error('test.ignore', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print('%10s  %r' % (encoding, codecs.decode('\xff', encoding, 'test.ignore')))

# Test codecs.register_error()

import codecs

def handler(exception):
    print(exception)
    return ('', exception.end)

codecs.register_error('test.ignore', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print('%10s  %r' % (encoding, codecs.decode('\xff', encoding, 'test.ignore')))

# Test codecs.register_error()

import codecs

def handler(exception):
    print(exception)
    return ('', exception.end)

cod
