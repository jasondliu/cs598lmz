import codecs
# Test codecs.register_error
reader = codecs.getreader('utf-16-le')('\xff\xfeA\x00B\x00C\x00', codecs.register_error(normalname="replace"))
reader.read()
decode('utf-16-le', '\xff\xfeA\x00B\x00C\x00', codecs.register_error(normalname="replace"))

# Test codecs.lookup_error
reader = codecs.StreamReader(codecs.LookupError(normalname="replace"))
reader.decode(b'\xff')

# Test 3-argument codecs.decode
encoding = 'utf-16'
def codecs_decode(bs, errors='strict'):
    return codecs.decode(bs, encoding, errors)

codecs.decode(b'\x00\x80', encoding, 'backslashreplace')
codecs.decode(b'\x00\x80', encoding, 'namereplace')
codecs.decode(b'\x00\x80', encoding
