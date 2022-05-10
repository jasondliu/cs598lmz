import codecs
# Test codecs.register_error("ignore", codecs.replace_errors)

# Test codecs.lookup("unknown")

# Test codecs.lookup("unknown").encode("abc")

# Test codecs.lookup("unknown").decode("abc")

# Test codecs.encode("abc", "unknown")

# Test codecs.decode("abc", "unknown")

# Test codecs.register_error("strict", None)
# ValueError: 'errorhandler' must not be None

# Test codecs.register_error("ignore", None)
# ValueError: 'errorhandler' must not be None

# Test codecs.lookup_error("strict")
# ValueError: unknown error handler name 'strict'

# Test codecs.lookup_error("ignore")
# ValueError: unknown error handler name 'ignore'

# Test codecs.lookup_error("strict").__name__
# TypeError: 'NoneType' object is not callable

# Test codecs.lookup_error("ignore").__name__
# TypeError: 'NoneType'
