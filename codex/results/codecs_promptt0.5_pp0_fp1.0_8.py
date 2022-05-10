import codecs
# Test codecs.register_error()

def my_handler(exception):
    return (u"", exception.end)

def my_handler_with_replace(exception):
    return (u"?", exception.end)

def my_handler_with_replace_and_bytes(exception):
    return (b"?", exception.end)

def my_handler_with_replace_and_bytes_wrong(exception):
    return (b"?", exception.end, b"")

def my_handler_with_replace_and_bytes_wrong2(exception):
    return (b"?", exception.end, b"", b"")

def my_handler_with_replace_and_bytes_wrong3(exception):
    return (b"?", exception.end, b"", b"", b"")

def my_handler_with_replace_and_bytes_wrong4(exception):
    return (b"?", exception.end, b"", b"", b"", b"")

def my_handler_with_replace_and_bytes_wrong5(exception):

