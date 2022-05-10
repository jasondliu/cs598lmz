import codecs
# Test codecs.register_error('test', codecs.replace_errors)
# codecs.register_error('test', codecs.ignore_errors)
# codecs.register_error('test', codecs.xmlcharrefreplace_errors)
# codecs.register_error('test', codecs.strict_errors)
# codecs.register_error('test', codecs.backslashreplace_errors)
# codecs.register_error('test', codecs.namereplace_errors)
codecs.register_error('test', codecs.lookup_error('strict'))

# Test codecs.lookup_error('strict')
# codecs.lookup_error('ignore')
# codecs.lookup_error('replace')
# codecs.lookup_error('xmlcharrefreplace')
# codecs.lookup_error('backslashreplace')
# codecs.lookup_error('namereplace')

# Test codecs.lookup('utf-8')
# codecs.lookup('ascii')
# codecs.lookup('latin-1')
# codec
