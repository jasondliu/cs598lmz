import codecs
# Test codecs.register_error()

import codecs

def my_error(exception):
    print("my_error:", exception)
    return ("", exception.start + 1)

codecs.register_error("test.myerrorhandler", my_error)

for encoding in ["ascii", "latin-1", "utf-8"]:
    print("Encoding:", encoding)
