import codecs
# Test codecs.register_error

def handler(exception):
    return (u"\ufffd", exception.end)

codecs.register_error("test.xmlcharrefreplace", handler)

# Test the error handler

print codecs.xmlcharrefreplace_errors("test.xmlcharrefreplace").encode(
    "ascii", "xmlcharrefreplace")

# Test the codec

print u"\u1234".encode("ascii", "xmlcharrefreplace")

# Test the incremental encoder

encoder = codecs.getincrementalencoder("ascii")("xmlcharrefreplace")
print encoder.encode(u"\u1234")
print encoder.encode(u"\u5678", True)

# Test the incremental decoder

decoder = codecs.getincrementaldecoder("ascii")("xmlcharrefreplace")
print decoder.decode("&#46;")
print decoder.decode("&#46;", True)
