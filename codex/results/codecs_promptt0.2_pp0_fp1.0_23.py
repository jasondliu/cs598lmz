import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test', handler)

print '%r' % '\x81'.decode('ascii', 'test')
print '%r' % '\x81'.decode('ascii', 'ignore')
print '%r' % '\x81'.decode('ascii', 'replace')
print '%r' % '\x81'.decode('ascii', 'xmlcharrefreplace')
print '%r' % '\x81'.decode('ascii', 'backslashreplace')
print '%r' % '\x81'.decode('ascii', 'namereplace')
print '%r' % '\x81'.decode('ascii', 'strict')
