import codecs
# Test codecs.register_error("replace_with_space")
codecs.register_error("replace_with_space", codecs.replace_with(" "))

# Test codecs.register_error("strict", None)
# codecs.register_error("strict", None)

# Test codecs.register_error("ignore", None)
codecs.register_error("ignore", None)

# Test codecs.register_error("xmlcharrefreplace")
codecs.register_error("xmlcharrefreplace", codecs.xmlcharrefreplace_errors)

# Test codecs.lookup_error("ignore")
codecs.lookup_error("ignore")

# codecs.lookup_error("strict")
# codecs.lookup_error("strict")

# codecs.lookup_error("replace")
codecs.lookup_error("replace")

# codecs.lookup_error("xmlcharrefreplace")
codecs.lookup_error("xmlcharrefreplace")

# codecs.lookup_error("backslashreplace")

