import codecs
# Test codecs.register_error('test', codecs.replace_errors)
a = b'\xc2\xc3'
codecs.register_error('test', codecs.replace_errors)
a.decode('utf-8', 'test')
codecs.register_error('strict', codecs.strict_errors)
