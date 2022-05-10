import codecs
# Test codecs.register_error

def handler(exception):
    return (u"", exception.end)

codecs.register_error("test.strict", handler)

# Test that the error handler is called
for encoding in ["ascii", "latin-1", "utf-8"]:
    print encoding
    try:
        unicode("\xff", encoding, "test.strict")
    except UnicodeDecodeError, e:
        print "Caught", e
        assert e.encoding == encoding
        assert e.object == "\xff"
        assert e.start == 0
        assert e.end == 1
        assert e.reason == "test.strict"
    else:
        print "No exception"

# Test that the error handler is called
for encoding in ["ascii", "latin-1", "utf-8"]:
    print encoding
    try:
        unicode("\xff", encoding, "test.strict")
    except UnicodeDecodeError, e:
        print "Caught", e
        assert e.encoding == encoding
        assert e.
