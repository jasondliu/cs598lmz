import codecs
# Test codecs.register_error(), should error with TclError for unknown codec
codecs.register_error('unknown', None)

# Test codecs.lookup_error(), should error with TclError for unknown codec
codecs.lookup_error('unknown')

# Test utf-8 error callback, should error with TclError
codecs.utf_8_decode('\xe9', 'strict', True)

# Test utf_7 error callback, should error with TclError
codecs.utf_7_decode('\xe9', 'strict', True)

# Test utf_16 error callback, should error with TclError
codecs.utf_16_decode('\xe9', 'strict', True)

# Test utf_16_be error callback, should error with TclError
codecs.utf_16_be_decode('\xe9', 'strict', True)

# Test utf_16_le error callback, should error with TclError
codecs.utf_16_le_decode('\xe9', 'st
