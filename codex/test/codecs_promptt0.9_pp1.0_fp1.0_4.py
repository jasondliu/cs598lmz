import codecs
# Test codecs.register_error.
# http://bugs.python.org/issue1376231
codecs.register_error("test.replace", codecs.replace_errors)
