import codecs
# Test codecs.register_error()

import codecs

def my_error(message):
    print("my_error:", message)
    return ("", 0)

codecs.register_error("test.my_error", my_error)

def my_decode(input, errors="strict"):
    print("my_decode:", repr(input), errors)
    return (input, len(input))

codecs.register(my_decode)

for encoding in ["test", "test.my_error"]:
    print("ENCODING:", encoding)
