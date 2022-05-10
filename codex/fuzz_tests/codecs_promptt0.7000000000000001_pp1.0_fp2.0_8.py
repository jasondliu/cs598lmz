import codecs
# Test codecs.register_error('strict', codecs.ignore_errors)

print(codecs.encode('abc\udcdc', 'idna'))
print(codecs.encode('abc\udcdc', 'idna', 'strict'))
print(codecs.encode('abc\udcdc', 'idna', 'ignore'))

print(codecs.encode('abc\udcdc', 'idna', 'replace'))
print(codecs.encode('abc\udcdc', 'idna', 'xmlcharrefreplace'))
