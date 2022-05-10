import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    print("my_error_handler:", exception)
    return ("", exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

for encoding in ["ascii", "latin-1", "utf-8"]:
    print("Encoding:", encoding)
