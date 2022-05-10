import codecs
# Test codecs.register_error()

import codecs

def handler(exc):
    return (u"", exc.end)

codecs.register_error("test", handler)

