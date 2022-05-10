import codecs
# Test codecs.register_error()
def custom_error(encoding):
    def bad_replace_error(err):
        print "Custom bad_replace_error"
        s = "Some error information: %r" % err.object[err.start:err.end]
        return (u'\ufffd' * len(s), err.start + len(s))
    return bad_replace_error
codecs.register_error("custom_error", custom_error)
u'\u8d23\u7f51\u7edc\u8d23\u7f51\u7edc'.encode('custom_error')
def custom_ignore_error(encoding):
    def bad_ignore_error(err):
        print "Custom bad_ignore_error"
        s = "Some error information: %r" % err.object[err.start:err.end]
        return (u'', err.end)
    return bad_ignore_error
codecs.register_error("custom_ignore_error", custom_ignore_error)
u'\u8d23\u7
