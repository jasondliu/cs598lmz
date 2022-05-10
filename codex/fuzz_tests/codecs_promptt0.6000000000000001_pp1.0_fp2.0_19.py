import codecs
# Test codecs.register_error
def bad_encode(exc):
    raise UnicodeError("Bad encoding")

codecs.register_error("test.bad_encode", bad_encode)

# Test that UnicodeError is raised
enc = codecs.getincrementalencoder("ascii")("test.bad_encode")
try:
    enc.encode(u"\u1234", "strict")
except UnicodeError as e:
    print(e)
