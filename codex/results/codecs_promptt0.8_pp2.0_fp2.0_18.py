import codecs
# Test codecs.register_error('fewbytes', codecs.lookup_error('strict'))
def my_error_handler(err):
    return u'', err.start + 1
codecs.register_error('fewbytes', my_error_handler)
test_unicode_encoding("utf-8", "ab\x80\x80\xc0", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                      "abxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
test_unicode_encoding("utf-8", "ab\x80\x80\xc0", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                      "abxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                      errorhandler='fewbytes')
test_unicode_encoding("rot-13", "abc\x80\x80xyz", "xxx\xe9\xe9yyy",
                      "xxx\xe9\xe9yyy",
                      errorhandler='ignore')
test_unicode_encoding("rot-13", "abc\x80\x80xyz", "xxx\xe9\xe9yyy",
                      "xxx\xe9\xe9yyy",
                      errorhandler='
