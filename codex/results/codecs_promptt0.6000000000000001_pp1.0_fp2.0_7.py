import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)
# codecs.register_error('strict', codecs.ignore_errors)
# assert codecs.lookup_error('strict') is codecs.ignore_errors
# codecs.register_error('strict', codecs.strict_errors)
# assert codecs.lookup_error('strict') is codecs.strict_errors
# codecs.register_error('strict', None)
# raises(LookupError, codecs.lookup_error, 'strict')

# Test codecs.lookup_error()
# raises(LookupError, codecs.lookup_error, 'xxx')

# Test codecs.charmap_encode()
# raises(TypeError, codecs.charmap_encode, 42, 'strict', {42: b'x'})
# raises(TypeError, codecs.charmap_encode, 'abc', 'strict', 42)
# raises(ValueError, codecs.charmap_encode, 'abc', 'strict', {})
