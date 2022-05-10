import codecs
# Test codecs.register_error()
import codecs

def handler(exception):
    print("->", exception)
    return ("%", 1)

codecs.register_error("my.my-error-handler", handler)

codecs.register_error("my.my-error-handler", handler)  # Second is ignored

codecs.register_error("my.my-error-handler", None)  # Disable handler

codecs.register_error("my.default", None)  # Disable just in case

codecs.register_error("my.my-error-handler", handler)

utf8 = "Hello, world\xa9".encode("UTF-8")
assert utf8 == b"Hello, world\xc2\xa9"
codecs.decode(utf8, "my.my-error-handler", "replace")
