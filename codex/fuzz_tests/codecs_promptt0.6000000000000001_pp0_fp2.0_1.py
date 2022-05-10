import codecs
# Test codecs.register_error

def bad_errorhandler(exception):
    raise exception

codecs.register_error("test.xmlcharrefreplace", bad_errorhandler)

# this should fail with an exception
codecs.register_error("test.xmlcharrefreplace", bad_errorhandler)
