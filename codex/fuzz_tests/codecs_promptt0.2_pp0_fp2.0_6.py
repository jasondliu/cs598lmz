import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print(exception)
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

s = 'abc\x80def'
print(s.decode('ascii', 'test.ignore'))

# Test codecs.register_error()

import codecs

def handler(exception):
    print(exception)
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

s = 'abc\x80def'
print(s.decode('ascii', 'test.ignore'))

# Test codecs.register_error()

import codecs

def handler(exception):
    print(exception)
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

s = 'abc\x80def'
print(s.decode('ascii', 'test.ignore'))

# Test
