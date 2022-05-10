import codecs
# Test codecs.register_error('strict', codecs.strict_errors)
# Test codecs.register_error('ignore', codecs.ignore_errors)
# Test codecs.register_error('replace', codecs.replace_errors)
# Test codecs.register_error('xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
# Test codecs.register_error('backslashreplace', codecs.backslashreplace_errors)

# Test codecs.lookup_error('strict')
# Test codecs.lookup_error('ignore')
# Test codecs.lookup_error('replace')
# Test codecs.lookup_error('xmlcharrefreplace')
# Test codecs.lookup_error('backslashreplace')

# Test codecs.register(lambda name: (lambda c, e: codecs.lookup(name).encode(c, e),
#                                    lambda c, e: codecs.lookup(name).decode(c, e),
#                                    None, None, None), 'utf-8')
# Test codecs.lookup('utf
