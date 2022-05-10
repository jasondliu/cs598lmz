import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    return (u"\ufffd", exception.end)

codecs.register_error("test", handler)

for encoding in ["utf-7", "utf-8", "utf-16", "utf-16-le", "utf-16-be",
                 "utf-32", "utf-32-le", "utf-32-be"]:
    print encoding
    print codecs.decode(u"\ufffe", encoding, "test")
    print codecs.decode(u"\uffff", encoding, "test")
    print codecs.decode(u"\U00010000", encoding, "test")
    print codecs.decode(u"\U00010001", encoding, "test")
    print codecs.decode(u"\U000ffffe", encoding, "test")
    print codecs.decode(u"\U000fffff", encoding, "test")
    print codecs.decode(u"\U00100000", encoding, "test")
    print codecs.
