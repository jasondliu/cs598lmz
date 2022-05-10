import codecs
# Test codecs.register_error.

import codecs

def handler(exception):
    return (u"\ufffd", exception.end)

codecs.register_error("test.xmlcharrefreplace", handler)

for encoding in ["ascii", "latin-1", "utf-8"]:
    print encoding
    print codecs.encode(u"\u1234", encoding, "test.xmlcharrefreplace")
    print codecs.encode(u"\u1234", encoding, "xmlcharrefreplace")
    print codecs.encode(u"\u1234", encoding, "ignore")
    print codecs.encode(u"\u1234", encoding, "replace")
    print codecs.encode(u"\u1234", encoding, "strict")
