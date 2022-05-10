import codecs
# Test codecs.register_error
def codec_name(input, errors='strict'):
    streamreader = codecs.getreader(unicode)(input, errors)
    test_string = u'string'
