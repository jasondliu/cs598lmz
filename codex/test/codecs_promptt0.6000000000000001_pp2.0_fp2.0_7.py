import codecs
# Test codecs.register_error()

def handler(exception):
    print(exception.__class__.__name__)
    return u'', exception.end

codecs.register_error('test', handler)

# Encoder
encoding = 'test'
codecs.register(lambda name: codecs.lookup('utf-8') if name == encoding else None)

# Decoder
codecs.register(lambda name: codecs.lookup('utf-8') if name == encoding else None)

s = u'\udce2\udce3\udce4\udce5' # unpaired surrogates

print(s.encode(encoding, 'test'))
print(s.encode(encoding, 'ignore'))
print(s.encode(encoding, 'replace'))
print(s.encode(encoding, 'xmlcharrefreplace'))
print(s.encode(encoding, 'backslashreplace'))

#print(s.encode(encoding, 'strict'))
