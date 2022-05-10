import codecs
# Test codecs.register_error

def handler(exception):
    print("handler:", exception)
    return ("?", exception.end)

codecs.register_error("test.lookup", handler)

def handler2(exception):
    print("handler2:", exception)
    return ("?", exception.end)

codecs.register_error("test.lookup2", handler2)

def handler3(exception):
    print("handler3:", exception)
    return ("?", exception.end)

codecs.register_error("test.lookup3", handler3)

def handler4(exception):
    print("handler4:", exception)
    return ("?", exception.end)

codecs.register_error("test.lookup4", handler4)

def handler5(exception):
    print("handler5:", exception)
    return ("?", exception.end)

codecs.register_error("test.lookup5", handler5)

def handler6(exception):
    print("handler6:", exception)
