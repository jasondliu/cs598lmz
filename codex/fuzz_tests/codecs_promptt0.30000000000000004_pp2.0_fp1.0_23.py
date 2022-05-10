import codecs
# Test codecs.register_error()

import codecs

def my_error_handler(exception):
    return (u'\ufffd', exception.end)

codecs.register_error('my_error', my_error_handler)

encoding = 'ascii'
text = u'\u00e0\u00e1\u00e2'

print text.encode(encoding, 'strict')
print text.encode(encoding, 'replace')
print text.encode(encoding, 'xmlcharrefreplace')
print text.encode(encoding, 'backslashreplace')
print text.encode(encoding, 'namereplace')
print text.encode(encoding, 'my_error')

print '-'*20

encoding = 'ascii'
text = u'\u00e0\u00e1\u00e2'

print text.encode(encoding, 'strict')
print text.encode(encoding, 'replace')
print text.encode(encoding, 'xmlcharrefreplace')

