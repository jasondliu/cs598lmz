import codecs
# Test codecs.register_error

def handler(exception):
    print("handler called")
    return ("", exception.end)

codecs.register_error("test.ignore", handler)

for encoding in ["ascii", "latin-1", "utf-8"]:
    print("Encoding:", encoding)
