import codecs
# Test codecs.register_error

SPAM = "spam"

def spam_error_handler(exception):
    return ("spam", exception.end)

codecs.register_error("test.spam_error_handler", spam_error_handler)

# Encode

assert codecs.charmap_encode(u"\uffff", "strict", {0xffff: SPAM}) == (SPAM, 1)
assert codecs.charmap_encode(u"\uffff", "test.spam_error_handler", {0xffff: SPAM}) == (SPAM, 1)

# Decode

assert codecs.charmap_decode("\x00\xff", "strict", {0xff: 0xffff}) == (u"\x00\uffff", 2)
assert codecs.charmap_decode("\x00\xff", "test.spam_error_handler", {0xff: 0xffff}) == (u"\x00\uffff", 2)
