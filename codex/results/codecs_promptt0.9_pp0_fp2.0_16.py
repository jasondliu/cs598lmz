import codecs
# Test codecs.register_error().
codecs.register_error("testerror", lambda e: (u"X", e.start + 1))
print codecs.lookup_error("testerror")
print codecs.lookup_error("testerrorkap")
