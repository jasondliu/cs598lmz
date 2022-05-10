import codecs
# Test codecs.register_error()

import codecs

def my_error(exception):
    print "my_error", exception
    return (u'', exception.end)

codecs.register_error("test.my_error", my_error)
print "register_error"

# Encode and decode
for encoding in ("ascii", "latin-1", "utf-8"):
    print encoding
    print codecs.encode("abc\xff", encoding, "test.my_error")
    print codecs.decode("abc\xff", encoding, "test.my_error")

# Incremental encode and decode
for encoding in ("ascii", "latin-1", "utf-8"):
    print encoding
    e = codecs.getincrementalencoder(encoding)("test.my_error")
    d = codecs.getincrementaldecoder(encoding)("test.my_error")
    print e.encode("abc\xff")
    print d.decode("abc\xff")

# Stream reader and writer
for encoding in ("
