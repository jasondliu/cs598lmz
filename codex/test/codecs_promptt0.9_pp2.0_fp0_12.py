import codecs
# Test codecs.register_error('test', codecs.ignore_errors) and codecs.lookup_error('test').
codecs.register_error('test', codecs.ignore_errors)
assert codecs.lookup_error('test') is codecs.ignore_errors
