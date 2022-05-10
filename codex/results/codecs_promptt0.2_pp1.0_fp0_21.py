import codecs
# Test codecs.register_error

import codecs

def my_error_handler(exception):
    print("my_error_handler:", exception)
    return (u"\ufffd", exception.end)

codecs.register_error("test.my_error_handler", my_error_handler)

def my_error_handler2(exception):
    print("my_error_handler2:", exception)
    return (u"\ufffd", exception.end)

codecs.register_error("test.my_error_handler2", my_error_handler2)

def my_error_handler3(exception):
    print("my_error_handler3:", exception)
    return (u"\ufffd", exception.end)

codecs.register_error("test.my_error_handler3", my_error_handler3)

def my_error_handler4(exception):
    print("my_error_handler4:", exception)
    return (u"\ufffd", exception.end)

codecs.register_error("test.
