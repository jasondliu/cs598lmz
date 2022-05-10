import codecs
# Test codecs.register_error
def handler(exception):
    return (u'', exception.end)
codecs.register_error("test.strict", handler)

u"abc".encode("test.strict")

def handler(exception):
    return (u'', exception.end)
codecs.register_error("test.strict", handler)

u"abc".encode("test.strict")

def handler(exception):
    return (u'', exception.end)
codecs.register_error("test.strict", handler)

u"abc".encode("test.strict")

def handler(exception):
    return (u'', exception.end)
codecs.register_error("test.strict", handler)

u"abc".encode("test.strict")

def handler(exception):
    return (u'', exception.end)
codecs.register_error("test.strict", handler)

u"abc".encode("test.strict")

def handler(exception):
    return
