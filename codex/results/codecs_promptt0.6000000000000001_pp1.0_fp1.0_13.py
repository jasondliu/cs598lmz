import codecs
# Test codecs.register_error()

def handler(exception):
    print("Error:", exception)

codecs.register_error("test.myhandler", handler)

# this should raise an error, and handler() should be called
codecs.decode("abc\xffdef\xff", "ascii", "test.myhandler")
