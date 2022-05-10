import codecs
# Test codecs.register_error()

# Test registering the same handler multiple times

import codecs

def handler(exception):
    return (u"XXX", exception.end)

def test(name):
    codecs.register_error(name, handler)
    codecs.register_error(name, handler)
    codecs.register_error(name, handler)
    codecs.register_error(name, handler)
    # Check that it's actually registered
    return codecs.lookup_error(name) is handler

print test("test1")
print test("test2")
print test("test3")
print test("test4")

print test("replace")
print test("xmlcharrefreplace")
print test("backslashreplace")
print test("namereplace")
print test("strict")
print test("ignore")
