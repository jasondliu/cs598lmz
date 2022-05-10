import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    print("handler called")
    return ("", exception.end)

codecs.register_error("test.strict", handler)

# Encode

encoder = codecs.getincrementalencoder("ascii")("strict")
encoder.errors = "test.strict"
encoder.encode("\x80")

# Decode

decoder = codecs.getincrementaldecoder("ascii")("strict")
decoder.errors = "test.strict"
decoder.decode("\x80")

# Stream reader

streamreader = codecs.getreader("ascii")(open("/dev/null", "rb"), "strict")
streamreader.errors = "test.strict"
streamreader.read()

# Stream writer

streamwriter = codecs.getwriter("ascii")(open("/dev/null", "wb"), "strict")
streamwriter.errors = "test.strict"
streamwriter.write("\x
