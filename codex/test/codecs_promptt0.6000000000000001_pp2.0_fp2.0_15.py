import codecs
# Test codecs.register_error("strict", codecs.strict_errors)
# Test codecs.register_error("ignore", codecs.ignore_errors)
# Test codecs.register_error("replace", codecs.replace_errors)

# The error handlers are registered under the name "test"
codecs.register_error("test", codecs.strict_errors)
codecs.register_error("test", codecs.ignore_errors)
codecs.register_error("test", codecs.replace_errors)

