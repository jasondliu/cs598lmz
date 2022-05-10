import codecs
# Test codecs.register_error

def handler(exception):
    return (u'', exception.end)

codecs.register_error('test.ignore', handler)

# Test that the error handler is called

u = u'\u3042\u3044\u3046\u3048\u304a'

for encoding in ['utf-8', 'utf-16', 'utf-16-le', 'utf-16-be']:
    for i in range(len(u)):
        s = u[:i].encode(encoding)
        t = s.decode(encoding, 'test.ignore')
        if t != u[:i]:
            print('Failed to ignore error')

# Test that the error handler is not called

u = u'\u3042\u3044\u3046\u3048\u304a'

