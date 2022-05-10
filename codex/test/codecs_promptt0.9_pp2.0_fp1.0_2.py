import codecs
# Test codecs.register_error().
# Try to decode a bogus UTF-8-encoded string.
codecs.register_error("drop", lambda e: (u"", e.start + 1))
