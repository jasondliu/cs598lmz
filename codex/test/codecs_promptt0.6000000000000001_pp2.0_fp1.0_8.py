import codecs
# Test codecs.register_error
def handler(exception):
    print("handler called:", exception)
    return ("@", 1)
codecs.register_error("test.ignore", handler)

def handler1(exception):
    print("handler1 called:", exception)
    return ("$", 1)
codecs.register_error("test.replace", handler1)

def handler2(exception):
    print("handler2 called:", exception)
    raise Exception("Cannot convert")

codecs.register_error("test.strict", handler2)

def handler3(exception):
    print("handler3 called:", exception)
    return ("&", exception.end)

codecs.register_error("test.backslashreplace", handler3)

def handler4(exception):
    print("handler4 called:", exception)
    return ("", exception.end)

codecs.register_error("test.xmlcharrefreplace", handler4)

def handler5(exception):
    print("handler5 called:", exception)
