import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.strict', handler)

# Test the handler

u = u'\u3042\u3044\u3046\u3048\u304a'

