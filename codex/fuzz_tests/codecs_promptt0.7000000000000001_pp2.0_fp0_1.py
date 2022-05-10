import codecs
# Test codecs.register_error, #1622.
import encodings
encodings.register_error("test.replace", codecs.replace_errors)
encodings.register_error("test.ignore", codecs.ignore_errors)
encodings.register_error("test.xmlcharrefreplace", codecs.xmlcharrefreplace_errors)
encodings.register_error("test.backslashreplace", codecs.backslashreplace_errors)

# Test codecs.lookup_error, #2826.
codecs.lookup_error("test.replace")
codecs.lookup_error("test.replace")
codecs.lookup_error("test.ignore")
codecs.lookup_error("test.xmlcharrefreplace")
codecs.lookup_error("test.backslashreplace")

# Test codecs.register_error, #2826.
codecs.register_error("test.replace", codecs.ignore_errors)
codecs.register_error("test.replace", codecs.replace_errors)
codecs.register
