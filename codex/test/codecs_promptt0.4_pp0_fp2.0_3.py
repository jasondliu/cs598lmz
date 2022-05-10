import codecs
# Test codecs.register_error
def my_error_handler(exception):
    print("my_error_handler:", exception)
    return ("?", exception.start + 1)
codecs.register_error("my_error", my_error_handler)

# Test UnicodeEncodeError
print("UnicodeEncodeError:")
