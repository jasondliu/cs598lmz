import codecs
# Test codecs.register_error("my_error", codecs.replace_errors)
# Test codecs.register_error("my_error", codecs.ignore_errors)
# Test codecs.register_error("my_error", codecs.report_errors)
# Test codecs.register_error("my_error", codecs.strict_errors)
# Test codecs.register_error("my_error", codecs.xmlcharrefreplace)
# Test codecs.register_error("my_error", codecs.backslashreplace)
# Test codecs.register_error("my_error", CodecInfo)
# Test codecs.register_error("my_error", lambda e: (u"?", e.start+1))

# Test codecs.lookup_error("my_error")


# Test decoding, encoding and incremental encoding with errors

def test_codecs(codecname, encinput, decinput, expected=None,
                encoding_errors=None, decoding_errors=None,
                incremental_encoding_errors=None,
                incremental_decoding_errors=None,
                incremental_
