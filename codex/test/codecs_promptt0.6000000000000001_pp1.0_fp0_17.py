import codecs
# Test codecs.register_error

def handler_function(exception):
    return ("?", exception.start + 1)

codecs.register_error("test.xlate", handler_function)

# codecs.lookup_error('strict') should return a function
# (in this case, the strict handler)
