import codecs
# Test codecs.register_error()

def handler(exception):
    return ("**", exception.end)

codecs.register_error("test.ignore", handler)

# This should raise an error even with the error handler
# (because "replace" will not be called since ignore=True)
try:
    codecs.utf_8_decode("\xff", "test.ignore", True)
except UnicodeDecodeError:
    pass
else:
    print("Should have raised UnicodeDecodeError")

# Now register a replace handler
def handler(exception):
    return ("*", exception.end)

codecs.register_error("test.replace", handler)

# This should not raise an error
codecs.utf_8_decode("\xff", "test.replace", True)

# Now register a replace handler
def handler(exception):
    return ("*", exception.end)

codecs.register_error("test.replace", handler)

# This should not raise an error
codecs.utf_8_decode("\xff", "test.replace
