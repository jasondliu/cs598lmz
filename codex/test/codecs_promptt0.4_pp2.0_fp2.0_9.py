import codecs
# Test codecs.register_error
codecs.register_error('strict', codecs.strict_errors)
codecs.register_error('ignore', codecs.ignore_errors)
codecs.register_error('replace', codecs.replace_errors)
codecs.register_error('xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
codecs.register_error('backslashreplace', codecs.backslashreplace_errors)

# Test codecs.lookup_error
assert codecs.lookup_error('strict') is codecs.strict_errors
assert codecs.lookup_error('ignore') is codecs.ignore_errors
assert codecs.lookup_error('replace') is codecs.replace_errors
assert codecs.lookup_error('xmlcharrefreplace') is codecs.xmlcharrefreplace_errors
assert codecs.lookup_error('backslashreplace') is codecs.backslashreplace_errors

# Test codecs.strict_errors
