import codecs
# Test codecs.register_error

encoding = 'xxx'

# The following call is harmless if 'xxx' isn't a known encoding.
codecs.register_error(encoding, codecs.strict_errors)
codecs.register_error(encoding, codecs.replace_errors)
codecs.register_error(encoding, codecs.ignore_errors)
codecs.register_error(encoding, codecs.xmlcharrefreplace_errors)
codecs.register_error(encoding, codecs.backslashreplace_errors)
