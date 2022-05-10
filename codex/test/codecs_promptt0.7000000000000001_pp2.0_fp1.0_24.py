import codecs
# Test codecs.register_error (Python 2 does not have it)
codecs.register_error('test-unicode-error', codecs.ignore_errors)
test_unicode_error = codecs.lookup_error('test-unicode-error')

# Test Unicode literal
u_literal = b'\xc3\xa5'

# Test unicode_internal_encode()
