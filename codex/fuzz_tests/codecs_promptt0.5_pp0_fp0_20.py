import codecs
# Test codecs.register_error
def search_function(encoding):
    if encoding != "test.searchfunction":
        return None
    return codecs.CodecInfo(
        name = "test.searchfunction",
        encode = codecs.lookup("utf-8").encode,
        decode = codecs.lookup("utf-8").decode,
        incrementalencoder = codecs.lookup("utf-8").incrementalencoder,
        incrementaldecoder = codecs.lookup("utf-8").incrementaldecoder,
        streamwriter = codecs.lookup("utf-8").streamwriter,
        streamreader = codecs.lookup("utf-8").streamreader,
    )
codecs.register(search_function)

def test_main():
    test_unicode_file(test_support.findfile("test_codecs.txt"))
    test_nonascii_file(test_support.findfile("test_codecs_cn.txt"))
    test_streamreader()
    test_incrementalencoder()
    test_incrementaldec
