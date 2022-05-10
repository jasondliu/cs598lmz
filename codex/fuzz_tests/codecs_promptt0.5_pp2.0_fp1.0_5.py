import codecs
# Test codecs.register_error
def codec_error_handler(exception):
    return (u'', exception.start + 1)
codecs.register_error("test.codec", codec_error_handler)
print(codecs.lookup_error("test.codec"))
print(codecs.strict_errors)
print(codecs.ignore_errors)
print(codecs.replace_errors)
print(codecs.backslashreplace_errors)
print(codecs.xmlcharrefreplace_errors)
# Test codecs.lookup_error
print(codecs.lookup_error("test.codec"))
print(codecs.lookup_error("strict"))
print(codecs.lookup_error("ignore"))
print(codecs.lookup_error("replace"))
print(codecs.lookup_error("backslashreplace"))
print(codecs.lookup_error("xmlcharrefreplace"))
# Test codecs.decode
print(codecs.decode("abc", "ascii", "strict
