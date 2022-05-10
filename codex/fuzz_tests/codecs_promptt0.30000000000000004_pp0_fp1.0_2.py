import codecs
# Test codecs.register_error

def handler(exception):
    return (u'', exception.end)

codecs.register_error("test.lookuperror", handler)

def handler(exception):
    return (u'', exception.end)

codecs.register_error("test.indexerror", handler)

def handler(exception):
    return (u'', exception.end)

codecs.register_error("test.keyerror", handler)

def handler(exception):
    return (u'', exception.end)

codecs.register_error("test.valueerror", handler)

def handler(exception):
    return (u'', exception.end)

codecs.register_error("test.zerodivisionerror", handler)

def handler(exception):
    return (u'', exception.end)

codecs.register_error("test.typeerror", handler)

def handler(exception):
    return (u'', exception.end)

codecs.register_error("test.attributeerror", handler
