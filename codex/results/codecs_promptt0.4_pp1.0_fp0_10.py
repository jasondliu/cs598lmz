import codecs
# Test codecs.register_error
def handler(exception):
    print "handler called"
    return (u"\uFFFD", exception.end)

codecs.register_error("test.xmlcharrefreplace", handler)

print codecs.xmlcharrefreplace_errors
print codecs.xmlcharrefreplace_errors["test.xmlcharrefreplace"]

codecs.xmlcharrefreplace_errors["test.xmlcharrefreplace"] = None

print codecs.xmlcharrefreplace_errors["test.xmlcharrefreplace"]
