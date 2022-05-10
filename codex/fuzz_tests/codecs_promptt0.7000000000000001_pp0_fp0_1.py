import codecs
# Test codecs.register_error
with codecs.open('somefile.txt', 'r', encoding='ascii', errors='replace') as fp:
    data = fp.read()
# Test codecs.lookup
utf_8 = codecs.lookup('utf-8')
print(utf_8.name)
print(utf_8.encode('abc'))
print(utf_8.decode(b'abc'))
# Test codecs.encode
print(codecs.encode('abc', 'ascii'))
print(codecs.encode('abc', 'base64'))
# Test codecs.decode
print(codecs.decode('abc', 'ascii'))
print(codecs.decode('YWJj', 'base64'))
# Test codecs.escape_decode
print(codecs.escape_decode(b'\\xa7'))
# Test codecs.escape_encode
print(codecs.escape_encode(b'\\xa7'))
