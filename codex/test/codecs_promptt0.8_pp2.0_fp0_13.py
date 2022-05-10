import codecs
# Test codecs.register_error('test', codecs.lookup_error('replace'))
codecs.register_error('test', codecs.lookup_error('replace'))
codecs.register_error('strict', codecs.lookup_error('strict'))

