import codecs
# Test codecs.register_error('strict', codecs.strict_errors)
# Test codecs.register_error('ignore', codecs.ignore_errors)
# Test codecs.register_error('replace', codecs.replace_errors)

def test_main():
    with test_support.check_py3k_warnings(quiet=True),\
         test_support.check_warnings(quiet=False,
                                     category=DeprecationWarning
                                     ):
        test_codecs()
        test_encodings()
        test_aliases()
        test_getencoder()
        test_getdecoder()
        test_getincrementalencoder()
        test_getincrementaldecoder()
        test_getreader()
        test_getwriter()
        test_streamreader()
        test_streamwriter()
        test_streamreaderwriter()
        test_incrementalencoder()
        test_incrementaldecoder()
        test_unicodeintern()
        test_codecs_cn()
        test_codecs_hk()
        test_cod
