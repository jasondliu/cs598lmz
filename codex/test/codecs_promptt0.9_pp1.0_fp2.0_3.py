import codecs
# Test codecs.register_error()
import codecs

def handler(exception):
    print("->", exception)
    return ("%", 1)

codecs.register_error("my.my-error-handler", handler)

codecs.register_error("my.my-error-handler", handler)  # Second is ignored

