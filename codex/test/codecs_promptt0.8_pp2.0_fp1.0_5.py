import codecs
# Test codecs.register_error:

def handler1(exception):
    return ('/', exception.end)

def handler2(exception):
    return ('/', 1)

