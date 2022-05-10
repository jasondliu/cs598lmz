import codecs
# Test codecs.register_error

SPAM = "spam"

def spam_error_handler(exception):
    return ("spam", exception.end)

codecs.register_error("test.spam_error_handler", spam_error_handler)

# Encode

