import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)
# Test codecs.register_error('ignore', codecs.ignore_errors)
# Test codecs.register_error('replace', codecs.replace_errors)
# Test codecs.register_error('xmlcharrefreplace', codecs.xmlcharrefreplace_errors)
# Test codecs.register_error('backslashreplace', codecs.backslashreplace_errors)

# Test codecs.lookup_error('strict')
# Test codecs.lookup_error('ignore')
# Test codecs.lookup_error('replace')
# Test codecs.lookup_error('xmlcharrefreplace')
# Test codecs.lookup_error('backslashreplace')

# Test codecs.open()
# Test codecs.EncodedFile()

# Test "universal newlines"
print(repr(codecs.open(TESTFN, encoding="ascii").read()))
print(repr(codecs.open(TESTFN, encoding="ascii", newline="").read()))

