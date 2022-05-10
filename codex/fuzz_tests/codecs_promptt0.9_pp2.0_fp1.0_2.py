import codecs
# Test codecs.register_error().
# Try to decode a bogus UTF-8-encoded string.
codecs.register_error("drop", lambda e: (u"", e.start + 1))
text_decoded = "some text".decode("utf-8", "drop")
print(text_decoded)  # prints u'some text'
# The above is just a demo of how codecs.register_error() works.
# It's not actually the best way to decode a string containing
# invalid UTF-8.
# Try to decode a bogus UTF-8-encoded string.
text_decoded = "some text".decode("utf-8", "replace")
print(text_decoded)  # prints u'some text\ufffd'
import sys
assert sys.stdout.encoding in ("UTF-8", "cp65001")
# Alternatively, specify coding:utf-8 on the first or second line
# of the Python source file.
