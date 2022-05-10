import codecs
# Test codecs.register_error("test_error", handler)

#
#  Not very useful test, tests only the 'strict' error handler
#

def handler(exception):
    print "!!! ENCODING ERROR HANDLER CALLED !!!"
    # return (unicode("XYZ"), exception.end)
    return (u"XYZ", exception.end)

print "TEST 1: encoder"
TEXT = u"\u3042\u3044"
TEST = codecs.getencoder("euc_jp")(TEXT)
print TEST

print "TEST 2: decoder"
TEXT = "ab"
TEST = codecs.getdecoder("euc_jp")(TEXT)
print TEST
print "TEST 3: stream reader"
TEXT = "ab"
stream = codecs.getreader("euc_jp")(StringIO.StringIO(TEXT))
print stream.read()
print "TEST 4: stream writer"
TEXT = u"\u3042\u3044"
stream = codecs.getwriter("euc_jp")(StringIO.
