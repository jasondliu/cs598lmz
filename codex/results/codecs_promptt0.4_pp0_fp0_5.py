import codecs
# Test codecs.register_error()

def my_error_handler(exception):
    print 'my_error_handler:', exception
    return (u'', exception.end)

codecs.register_error('test.lookup', my_error_handler)

s = u'pi: \u03c0'
encoded = s.encode('ascii', 'test.lookup')
print repr(encoded)

print '%r' % (u'\uFFFD',)

# Test codecs.register_error() with 'xmlcharrefreplace'

codecs.register_error('test.xmlcharrefreplace', codecs.xmlcharrefreplace_errors)

s = u'pi: \u03c0'
encoded = s.encode('ascii', 'test.xmlcharrefreplace')
print repr(encoded)

# Test codecs.register_error() with 'ignore'

codecs.register_error('test.ignore', codecs.ignore_errors)

s = u'pi: \u03c0'
encoded =
