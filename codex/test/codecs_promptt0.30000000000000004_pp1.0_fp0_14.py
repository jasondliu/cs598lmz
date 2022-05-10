import codecs
# Test codecs.register_error()

def handler(ex):
    return (u'', ex.start + 1)

codecs.register_error('test', handler)

