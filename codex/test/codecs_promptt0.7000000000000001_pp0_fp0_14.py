import codecs
# Test codecs.register_error, bug #1268574
codecs.register_error('e', codecs.ignore_errors)

# Test that the null character can be decoded in text mode
