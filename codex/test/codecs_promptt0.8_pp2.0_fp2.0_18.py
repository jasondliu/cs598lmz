import codecs
# Test codecs.register_error('fewbytes', codecs.lookup_error('strict'))
def my_error_handler(err):
    return u'', err.start + 1
codecs.register_error('fewbytes', my_error_handler)
