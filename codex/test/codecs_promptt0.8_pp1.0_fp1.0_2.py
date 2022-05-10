import codecs
# Test codecs.register_error("ignore")
codecs.register_error("ignore", lambda err: (u"\ufffd", err.start + 1))

