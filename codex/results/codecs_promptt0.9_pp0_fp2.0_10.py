import codecs
# Test codecs.register_error:
def errFunc():
    while True:
        yield u'\u0082'
        yield '\ufffd'
encoding.register_error("testCodec", errFunc)
# Test codecs.lookup:
def badCodec():
    pass
err = False
try:
    codecs.lookup("badCodec")
except KeyError:
    err = True
assert err, "OK"
try:
    codecs.lookup("badCodec")
except KeyError:
    pass
assert encoding.lookup("testCodec").name == "testCodec"
assert encoding.lookup("testCodec").decode == errFunc().next # works????
try:
    encoding.codecs
except AttributeError:
    pass
try:
    encoding.lookup("testCodec")
except AttributeError:
    pass
try:
    encoding.register_error("testCodec", errFunc)
except AttributeError:
    pass
class testReader:
    
    def encode(self, data):
        return [u'
