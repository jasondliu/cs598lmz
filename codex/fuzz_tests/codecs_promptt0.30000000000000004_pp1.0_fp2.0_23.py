import codecs
# Test codecs.register_error()

def handler(exception):
    print "handler called"
    return u"\ufffd", exception.end

codecs.register_error("test.lookup", handler)

encoding = "test.lookup"

# Encode

print "Encode"

for input in [u"abc", u"\u3042", u"\u3042\u3042", u"\u3042\u3042\u3042"]:
    print "input", repr(input)
    for errors in ["strict", "ignore", "replace", "test.lookup"]:
        print "errors", errors
        print "output", repr(input.encode(encoding, errors))

# Decode

print "Decode"

for input in ["abc", "\x82\xa0", "\x82\xa0\x82\xa0", "\x82\xa0\x82\xa0\x82\xa0"]:
    print "input", repr(input)
    for errors in ["strict", "ignore", "replace", "
