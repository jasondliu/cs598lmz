import codecs
# Test codecs.register_error()

def bad_errorhandler(exception):
    print 'bad_errorhandler:', exception
    return ('&', 1)

codecs.register_error('test.bad', bad_errorhandler)
print codecs.lookup_error('test.bad')
# The Codec failed
print codecs.utf_8_encode('hello')
# The Codec succeeded
print codecs.utf_8_encode(u'\U00012345')
