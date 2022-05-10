import codecs
# Test codecs.register_error()
codecs.register_error('error', codecs.replace_errors)
