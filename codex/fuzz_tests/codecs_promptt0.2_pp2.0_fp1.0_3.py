import codecs
# Test codecs.register_error

import codecs

def test(name):
    print name, ":",
    try:
        codecs.lookup_error(name)
    except LookupError:
        print "not found"
    else:
        print "found"

test("ignore")
test("replace")
test("xmlcharrefreplace")
test("backslashreplace")
test("namereplace")
test("strict")
test("surrogateescape")
test("surrogatepass")
test("notanerrorhandler")
