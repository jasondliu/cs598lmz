import codecs
# Test codecs.register_error('strict', codecs.strict_errors)

# Test codecs.register_error('ignore', codecs.ignore_errors)

# Test codecs.register_error('replace', codecs.replace_errors)

# Test codecs.register_error('xmlcharrefreplace', codecs.xmlcharrefreplace_errors)

# Test codecs.register_error('backslashreplace', codecs.backslashreplace_errors)

def test_main():
    test_support.run_unittest(CodecsModuleTest, ErrorHandlingTest)
    test_support.run_doctest(codecs)

