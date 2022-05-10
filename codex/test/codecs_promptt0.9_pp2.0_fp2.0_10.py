import codecs
# Test codecs.register_error first
# so that exceptions can be imported if necessary.
codecs.register_error('test', codecs.strict_errors)

