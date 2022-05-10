import codecs
# Test codecs.register_error

def handler(exception):
    print("handler called")
    return (u"\ufffd", exception.end)

codecs.register_error("test.myhandler", handler)

# Test that the handler is called
