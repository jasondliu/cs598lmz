import codecs
# Test codecs.register_error
def handler_error(exception):
    print("Error:", exception)
    return ("", exception.end)
codecs.register_error("test.strict", handler_error)
codecs.register_error("test.ignore", handler_error)
codecs.register_error("test.replace", handler_error)
codecs.register_error("test.xmlcharrefreplace", handler_error)
codecs.register_error("test.backslashreplace", handler_error)
# Test codecs.lookup
print(codecs.lookup("utf-8"))
# Test codecs.lookup_error
print(codecs.lookup_error("test.strict"))
print(codecs.lookup_error("test.ignore"))
print(codecs.lookup_error("test.replace"))
print(codecs.lookup_error("test.xmlcharrefreplace"))
print(codecs.lookup_error("test.backslashreplace"))
# Test codecs.getencoder
