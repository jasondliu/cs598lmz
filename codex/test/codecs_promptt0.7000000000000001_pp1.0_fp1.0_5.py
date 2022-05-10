import codecs
# Test codecs.register_error
# Only the 'strict' handler is important here
# The others are needed to test a different path in the code
def replace_handler(exception):
    return (u"?", exception.end)

codecs.register_error("test.replace", replace_handler)
codecs.register_error("test.ignore", codecs.ignore_errors)
codecs.register_error("test.xmlcharrefreplace", codecs.xmlcharrefreplace_errors)
codecs.register_error("test.backslashreplace", codecs.backslashreplace_errors)
# End test codecs.register_error

def encode(input, errors="strict"):
    return (input.encode("ascii", errors), len(input))

