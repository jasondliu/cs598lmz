import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'', exception.end

codecs.register_error('test', handler)

print '%r' % u'\u1234'.encode('ascii', 'test')

# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'', exception.end

codecs.register_error('test', handler)

print '%r' % u'\u1234'.encode('ascii', 'test')

# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'', exception.end

codecs.register_error('test', handler)

print '%r' % u'\u1234'.encode('ascii', 'test')

# Test codecs.register_error()

import codecs

def handler(exception):

